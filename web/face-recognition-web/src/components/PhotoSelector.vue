<template>
    <div class="photo-selector">
        <video v-if="useVideo" ref="video" :width="videoWidth" :height="videoHeight">
        </video>
        <img v-else="useVideo" :src="imgSrc" alt="people" class="upload-img" @click="selectFile" />
        <input type="file" ref="filed" hidden="" @change="filePreview" accept="image/jpeg, image/png" />
        <div class="button-box">
            <el-switch v-model="useVideo" style='zoom: 1.4;' active-text="摄像头" @change="switchVideo" />
            <el-button type="primary" :icon="captureIcon" style="zoom:1.5" v-if="useVideo" @click="captureImage" />
        </div>
    </div>
    <canvas ref="canvasElement" style="display: none;"></canvas>
</template>

<script>
import { Camera } from '@element-plus/icons-vue'

export default {
    name: 'PhotoSelector',
    components: {
        Camera,
    },
    data() {
        return {
            videoHeight: 480,
            videoWidth: 320,
            useVideo: false,
            imgSrc: "people.png",
            imgFile: null,
            isSelected: false,
            captureIcon: Camera,
        }
    },
    mounted() {

    },
    methods: {
        switchVideo() {
            if (this.useVideo) {
                this.openVideo();
            } else {
                this.closeVideo();
            }
        },
        selectFile() {
            this.$refs.filed.click();
        },
        filePreview(event) {
            this.imgFile = event.target.files[0];
            if (!this.imgFile || !this.imgFile.type.startsWith('image/')) {
                return;
            }
            let reader = new FileReader();
            reader.readAsDataURL(this.imgFile);
            reader.onload = () => {
                this.imgSrc = reader.result;
                this.isSelected = true;
            }
        },
        closeVideo() {
            if (this.$refs.video && this.$refs.video.srcObject) {
                this.$refs.video.pause();
                this.$refs.video.srcObject.getTracks().forEach(track => track.stop());
                this.$refs.video.srcObject = null;
            }
        },
        openVideo() {
            navigator.mediaDevices.enumerateDevices()
                .then(devices => {
                    let device = devices.find(device => {
                        if (device.kind === 'videoinput') {
                            return true;
                        }
                    })
                    navigator.mediaDevices.getUserMedia({
                        video: {
                            width: this.$data.videoWidth,
                            height: this.$data.videoHeight,
                            deviceId: device.deviceId
                        }
                    })
                        .then(stream => {
                            this.$refs.video.srcObject = stream;
                            this.$refs.video.play();
                        })
                        .catch(err => {
                            console.log(err)
                        });
                })
        },
        captureImage() {
            let videoElement = this.$refs.video;
            let canvasElement = this.$refs.canvasElement;
            canvasElement.width = videoElement.width;
            canvasElement.height = videoElement.height;
            let context = canvasElement.getContext('2d');
            context.drawImage(videoElement, 0, 0, videoElement.width, videoElement.height);
            let imageData = canvasElement.toDataURL('image/png');
            let link = document.createElement('a');
            link.href = imageData;
            link.download = 'screenshot.png';
            link.click();
        },
    }
};

</script>

<style scoped>
.photo-selector {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 2vh;
}

.upload-img {
    max-width: 320px;
    max-height: 480px;
}

.upload-img:hover {
    cursor: pointer;
}

.button-box {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 2vh;
}
</style>