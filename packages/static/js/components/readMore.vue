<template>
<div>
    <button class="btn btn-success" @click="getPackageUrl(packageName)">Read more</button>

    <div v-if="showCommandLine">
        <installCommand :packagename="packageName"></installCommand>
    </div>
</div>
</template>

<script>
export default {
    props: ['packageName', 'packageid', 'showCommandLine'],
    data: function() {
        return {
            loading: false,
            isPage: false
        }
    },
    methods: {
        getPackageUrl(id){
            store.state.isPage = true
            this.isPage = true
        }
    }
}
</script>