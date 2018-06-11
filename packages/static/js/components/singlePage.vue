<template>
    <div class="col-md-4">
    <div class="card mb-12">
        <img class="card-img-top" :src="package.server.icon" alt="Card image cap">
        <div class="card-body">
            <h2 class="card-title">{{ package.packageArgs.softwareName }}</h2>
            <p class="card-text">{{ package.packageArgs.description }}</p>
            
            <h5 class="card-title">Dependencies:</h5>
            <p class="card-text">
                <span v-for="package in package.packageArgs.dependencies"> {{ package }}</span>
            </p>
        </div>
        <div class="card-footer text-muted">
            Version
            <a href="#">{{ package.packageArgs.version }}</a>
        </div>
        </div>
    </div>
</template>

<script>
export default {
    props: ['packagename', 'packageid'],
    data: function() {
        return {
            package: [],
            loading: true,
            isPage: false
        }
    },
    mounted: function() {
        this.getPackage(this.packageid)
    },
    methods: {
        getPackage(id) {
            axios.get(`/api/packages/`+id)
            .then((response) => {
                this.package = response.data
                this.loading = false;
            })
            .catch((err) => {
                this.loading = false;
                console.log(err);
            })
        },
    }
}
</script>

<style>

</style>
