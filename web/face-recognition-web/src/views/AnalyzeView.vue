<template>
    <div class="main-analyze">
        <PhotoSelector ref="photoSelect" />
        <el-button :loading="is_loading" type="primary" @click="analyze" style="height: 50px; font-size: 20px;">Analyze</el-button>
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
        analyze() {
            if (this.$refs.photoSelect.$data.isSelected) {
                const formData = new FormData();
                formData.append('image', this.$refs.photoSelect.$data.imgFile);
                this.is_loading = true;
                axios.post('/api/upload', formData)
                    .then(response => {
                        if (response.data.status === 1) {
                            let imgId = response.data.img_id;
                            axios.post('/api/analyze', {
                                img_id: imgId,
                            })
                                .then(response2 => {
                                    this.$alert(
                                        '<div><strong>Age</strong>: ' + response2.data.results[0].age + '</div>'
                                        + '<div><strong>Gender</strong>: ' + response2.data.results[0].dominant_gender + '</div>'
                                        + '<div><strong>Emotion</strong>: ' + response2.data.results[0].dominant_emotion + '</div>'
                                        + '<div><strong>Race</strong>: ' + response2.data.results[0].dominant_race + '</div>', 'Result', {
                                            confirmButtonText: 'confirm',
                                            dangerouslyUseHTMLString: true,
                                        }
                                    );
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
.main-analyze {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 2vh;
}
</style>