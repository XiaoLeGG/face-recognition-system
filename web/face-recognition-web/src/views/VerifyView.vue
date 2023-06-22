<template>
    <div class="main-verify">
        <div class="photos-box">
            <PhotoSelector ref="photoSelect1" />
            <PhotoSelector ref="photoSelect2" />
        </div>
        <el-button :loading="is_loading" type="primary" @click="verify" style="height: 50px; font-size: 20px;">Verify</el-button>
    </div>
</template>

<script>
import PhotoSelector from '../components/PhotoSelector.vue';
import axios from 'axios';

export default {
    beforeRouteLeave(to, from, next) {
        this.$refs.photoSelect1.closeVideo();
        this.$refs.photoSelect2.closeVideo();
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
        verify() {
            if (!this.$refs.photoSelect1.$data.isSelected || !this.$refs.photoSelect2.$data.isSelected) {
                this.$message({
                    message: 'Please select two photos',
                    type: 'warning'
                });
                return;
            }
            const formData1 = new FormData();
            formData1.append('image', this.$refs.photoSelect1.$data.imgFile);
            const formData2 = new FormData();
            formData2.append('image', this.$refs.photoSelect2.$data.imgFile);
            this.is_loading = true;
            axios.post('/api/upload', formData1)
                .then(response1 => {
                    if (response1.data.status === 1) {
                        axios.post('/api/upload', formData2)
                            .then(response2 => {
                                if (response2.data.status === 1) {
                                    axios.post('/api/verify', {
                                        img_id1: response1.data.img_id,
                                        img_id2: response2.data.img_id,
                                    })
                                    .then(response3 => {
                                        this.$alert(response3.data.verified === 'True' ? 'Verification pass' : 'Verification failed', 'Result', {
                                            confirmButtonText: 'Confirm',
                                        });
                                        this.is_loading = false;
                                    })
                                    .catch(error => {
                                        console.log(error);
                                        this.is_loading = false;
                                    });
                                } else {
                                    this.$message(
                                        {
                                            message: response2.data.message,
                                            type: 'error'
                                        }
                                    );
                                    this.is_loading = false;
                                }
                            })
                            .catch(error => {
                                console.log(error);
                                this.is_loading = false;
                            });
                    } else {
                        this.$message(
                            {
                                message: response1.data.message,
                                type: 'error'
                            }
                        );
                        this.is_loading = false;
                    }
                })
                .catch(error => {
                    console.log(error);
                    this.is_loading = false;
                });
        }
    }
}

</script>

<style scoped>
.main-verify {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 2vh;
}

.photos-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2vw;
}

</style>