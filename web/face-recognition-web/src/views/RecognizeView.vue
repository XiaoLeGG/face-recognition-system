<template>
    <div class="main-recognize">
        <PhotoSelector ref="photoSelect" />
        <el-button :loading="is_loading" type="primary" @click="recognize" style="height: 50px; font-size: 20px;">Recognize</el-button>
    </div>
</template>

<script>
import PhotoSelector from '../components/PhotoSelector.vue';
import axios from 'axios';

export default {
    beforeRouteLeave(to, from, next) {
        this.$refs.photoSelect.closeVideo();
        next();
    },
    components: {
        PhotoSelector,
    },
    data() {
        return {
            is_loading: false,
        }
    },
    methods: {
        recognize() {
            if (this.$refs.photoSelect.$data.isSelected) {
                const formData = new FormData();
                formData.append('image', this.$refs.photoSelect.$data.imgFile);
                this.is_loading = true;
                axios.post('/api/upload', formData)
                    .then(response => {
                        if (response.data.status === 1) {
                            let imgId = response.data.img_id;
                            axios.post('/api/recognize', {
                                img_id: imgId,
                            })
                                .then(response2 => {
                                    if (response2.data.status === 1) {
                                        this.$alert('Welcome back, ' + response2.data.user + '!', 'Recognization Success', {
                                            confirmButtonText: 'confirm',
                                        })
                                    } else {
                                        this.$message(
                                            {
                                                message: response2.data.message,
                                                type: 'error'
                                            }
                                        );
                                    }
                                    this.is_loading = false;
                                })
                                .catch(error => {
                                    this.$message(
                                        {
                                            message: error,
                                            type: 'error'
                                        }
                                    );
                                    this.is_loading = false;
                                });
                        } else {
                            this.$message(
                                {
                                    message: response.data.message,
                                    type: 'error'
                                }
                            );
                            this.is_loading = false;
                        }
                    })
                    .catch(error => {
                        this.$message(
                            {
                                message: error,
                                type: 'error'
                            }
                        );
                        this.is_loading = false;
                    });
            } else {
                this.$message({
                    message: 'Please select a photo',
                    type: 'warning'
                });
            }
        }
    }
}

</script>

<style scoped>
.main-recognize {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 2vh;
}
</style>