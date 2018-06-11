<template>

<div>
<button class="btn btn-info" @click="goBack()" v-if="isPage == true"> Go back</button>
<package-page :packageName="packageName" :packageid="packageId"  v-if="isPage == true"></package-page>

<table class="table" v-if="isPage == false">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Package</th>
        <th scope="col">Version</th>
        <th scope="col">Action</th>
        </tr>
    </thead>
    <tbody>
        <tr v-for="package in packages.results">
        <th scope="row" ><img :src="package.server.icon" alt="" width="50" height="50"></th>
        <th scope="row" >{{package.packageArgs.softwareName}} <br> {{ package.packageArgs.description }}</th>
        <th scope="row" >{{package.packageArgs.version}}</th>
        <!-- <td>${package}</td> -->
        <td>
            <installButton :packageName="package.packageArgs.packageName" :packageid="package.id" @click.native="showPage(package.packageArgs.packageName, package.id)"></installButton>
        </td>
        </tr>
    </tbody>
</table>



<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#" v-if="packages.previous != null" @click="getPackages(previousUrl)">Previous</a></li>
    <li class="page-item" v-for="num in countPageNumber"><a class="page-link" @click="getPackages(nextUrl)">{{ num }}</a></li>
    <li class="page-item"><a class="page-link"  v-if="packages.next != null" @click="getPackages(nextUrl)">Next</a></li>
  </ul>
</nav>


</div>
    
</template>

<script>
export default {
  props: ["maxentry"],
  data: function() {
    return {
      message: null,
      nextUrl: null,
      previousUrl: null,
      count: null,
      isPage: false,
      packageName: null,
      packageId: null,
      packages: []
    };
  },
  
  computed: {
    countPageNumber: function() {
        var totalPageNumber = Math.round(this.count / this.maxentry)
        return totalPageNumber
    }
  },

  mounted: function() {
    this.getPackages();
    this.countPageNumber
    
  },


  methods: {
    getPackages: function(url = "/api/packages") {
      if (url != "/api/packages"){
        this.isPage = true;
      }

      this.loading = true;
      axios
        .get(url)
        .then(response => {
          this.packages = response.data
          this.count = response.data.count
          this.nextUrl = response.data.next
          this.previousUrl = response.data.previous
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    },

    showPage: function(packageName, packageId){
        this.packageName = packageName
        this.packageId = packageId
        this.isPage = true

    },


    goBack: function(){
        this.isPage = false
    }
  }
};
</script>
