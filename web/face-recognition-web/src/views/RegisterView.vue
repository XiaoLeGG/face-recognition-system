<template>
    <div class="main-register">
        <div class="box">
            <PhotoSelector ref="photoSelect" />
        </div>
        <div class="box">
            <div class="parameter-box">
                <el-input v-model="name" placeholder="Please input your name"
                    style="width: 300px; height: 50px; font-size: 20px;" />
                <div class="button-box">
                    <el-button type="primary" :loading="is_loading" @click="register" style="height: 50px; font-size: 20px;">Register</el-button>
                </div>
            </div>
        </div>
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
            name: '',
            is_loading: false,
        }
    },
    methods: {
        register() {
            if (this.name === '') {
                this.$message({
                    message: 'Please input your name',
                    type: 'warning'
                });
                return;
            }
            if (this.$refs.photoSelect.$data.isSelected) {
                const formData = new FormData();
                formData.append('image', this.$refs.photoSelect.$data.imgFile);
                this.is_loading = true;
                axios.post('/api/upload', formData)
                    .then(response => {
                        if (response.data.status === 1) {
                            
                            let imgId = response.data.img_id;
                            axios.post('/api/register', {
                                img_id: imgId,
                                name: this.name,
                            })
                            .then(response2 => {
                                if (response2.data.status === 1) {
                                    this.$message(
                                        {
                                            message: response2.data.message,
                                            type: 'success'
                                        }
                                    );
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
                                        message: 'Registration failed',
                                        type: 'error'
                                    }
                                );
                                this.is_loading = false;
                            });
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
        },
    }
}

</script>

<style scoped>
.main-register {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
}

.box {
    display: flex;
    height: 600px;
    width: 400px;
    border-left: 1px solid var(--color-border);
    justify-content: center;
    /* background-color: red; */
}

.parameter-box {
    display: flex;
    flex-direction: column;
    align-items: left;
    gap: 2vh;
    justify-content: center;
    height: 100%;
}

.box:first-of-type {
    border: 0;
    margin-right: 4vh;
}
</style>