<template>
<div>
    <button class="btn btn-success" @click="getPackageUrl(packageName)">Read more</button>

    <div v-if="commandLine">
        <installCommand :packagename="packagename"></installCommand>
    </div>
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
        }
    }
}
</script>

<style>

</style>
