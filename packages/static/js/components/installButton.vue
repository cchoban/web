<template>
<div>
    <button class="btn btn-success" @click="getPackageUrl(packageName)">Install</button>
    </div>
</template>

<script>
export default {
    props: ['packageName', 'packageid'],
    data: function() {
        return {
            loading: false,
            isPage: false
        }
    },
    methods: {
        getPackageUrl(id){
            this.isPage = true
            // setTimeout(() => {
            //     window.location.href = "/packages/"+id
            // }, 200);
        }
    }
}
</script>

<style>

</style>
