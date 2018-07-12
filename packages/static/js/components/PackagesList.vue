<template>

<div>

<button class="btn btn-info" @click="goBack()" v-if="isPage == true" style="width:100%;margin:20px"> Go back</button>
<package-page :packagename="packageName" :packageid="packageId" v-if="isPage == true"></package-page>


<div class="container" v-if="isPage == false">
<div class="search card card-body" style="margin-bottom:30px">
  <h3>Search for your favorite software</h3>
  <p class="lead">
    Let me know your software name!
  </p>
  <form action="/" method="post">
    <input type="text" name="packageName" class="form-control" placeholder="Software Name" v-model="search_key" >
    <br>
    <button class="btn btn-success" v-on:click.prevent="getPackages()">Search</button>
  </form>
</div>

<table class="table" v-if="packages.results.length > 0">
    <thead>
        <tr>
        <th scope="col">#</th>
        <th scope="col">Package</th>
        <th scope="col">Version</th>
        <th scope="col">Action</th>
        </tr>
    </thead>
    <tbody >
        <tr v-for="package in packages.results">
        <th scope="row" ><img :src="package.server.icon" alt="" width="50" height="50"></th>
        <th scope="row" >{{package.packageArgs.softwareName}} <br> {{ package.packageArgs.description }}</th>
        <th scope="row" >{{package.packageArgs.version}}</th>
        <!-- <td>${package}</td> -->
        <td>
            <readMore :packageName="package.packageArgs.packageName" :packageid="package.id" @click.native="showPage(package.packageArgs.packageName, package.id)"></readMore>
            <installCommand :packagename="package.packageName"></installCommand>
        </td>
        </tr>
    </tbody>
</table>
  <div v-else>
    <div class="alert alert-info">
        No packages found with name of <b>{{ search_key }}</b>
    </div>
  </div>



<nav aria-label="Page navigation example">
  <ul class="pagination">
    <li class="page-item"><a class="page-link" href="#" v-if="packages.previous != null" @click="getPackages(previousUrl)">Previous</a></li>
    <li class="page-item" v-for="(num, pages) in countPageNumber"><a class="page-link" @click="getPackages('http://localhost:8000/api/packages/?limit=10&offset='+num)">{{ pages }}</a></li>
    <li class="page-item"><a class="page-link"  v-if="packages.next != null" @click="getPackages(nextUrl)">Next</a></li>
  </ul>
</nav>


</div>
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
      packages: [],
      search_key: ""
    };
  },

  computed: {
    countPageNumber: function() {
      var totalPageNumber = Math.ceil(this.count / this.maxentry);

      var pages = {}
      var offset = -10
      for (var page=1;page<=totalPageNumber;page++){
          pages[page]= offset +=10
      }
      return pages;
    }
  },

  mounted: function() {
    this.getPackages();
    this.countPageNumber;
  },

  methods: {
    getPackages: function(url = "/api/packages") {
      // if (
      //   url != "/api/packages" &&
      //   url != this.nextUrl &&
      //   url != this.previousUrl
      // ) {
      //   this.isPage = true;
      // }
      if (this.search_key !== "") {
        url = `/api/packages/?search=${this.search_key}`;
      }

      this.loading = true;
      axios
        .get(url)
        .then(response => {
          this.packages = response.data;
          this.count = response.data.count;
          this.nextUrl = response.data.next;
          this.previousUrl = response.data.previous;
          this.loading = false;
        })
        .catch(err => {
          this.loading = false;
          console.log(err);
        });
    },

    showPage: function(packageName, packageId) {
      this.packageName = packageName;
      this.packageId = packageId;
      this.isPage = true;
    },

    goBack: function() {
      this.isPage = false;
      history.pushState(null, null, "/packages");
    }
  }
};
</script>
