<template>
    <div>
    <div class="ui container two column fluid left">
        <div class="ui section column twentyfivepx">
            <h2>{{ category_name }}</h2>
                <div>
                    <div class="featured-podcast" :style="'background-image: linear-gradient(to top, black, transparent), url('+category_image+')'">
                        <h1>{{ category_name }}</h1>
                        <div class="info">sd</div>
                    </div>
                </div>
            </div>
        </div>

        <div class="ui column content">
            <div class="header">
                <div class="section-image">
                    <img :src="category_image" alt="sa">
                </div>
                <h1 class="bold catname"> {{ category_name }} </h1>
            </div>


            <div class="ui column posts post-content">
                <div class="post" v-for="package in packages">
                    <div class="header-section">
                        <div class="image">
                            <img :src="package.server.icon" alt="">
                        </div>
                        <div class="title">
                            <h2>
                                <a :href="'/packages/'+package.packageName"> {{ package.packageName }} </a> 
                            </h2>
                        </div>
                        <div class="author">
                            <i class="icon bookmark outline"></i>
                            <i class="icon external alternate"></i>
                            <a href="#" class="author-name"> {{ package.user }} </a>
                            <span class="bold time"> <timeago :since="package.created_at"></timeago> </span>
                        </div>
                    </div>

                    <div class="description">
                        <p>
                            {{ package.packageArgs.description }}
                        </p>
                    </div>
                </div>
            </div>
        </div>
        <!-- #Content -->
    </div>
    </div>
</template>

<script>
export default {
  props: ["category", "category_name"],
  data: function() {
    return {
      packages: [],
      nextUrl: null,
      previousUrl: null,
      category_image: ""
    };
  },
  beforeMount: function() {
    this.grabPackages();
    $('.root').addClass("main")
  },

  methods: {
    grabPackages: function() {
      var url = "/api/packages/?category=" + this.category;
      axios.get(url).then(response => {
        this.packages = response.data.results;
        this.selectRandomImage();
      });
    },
    selectRandomImage: function() {
      var i;
      var rand = this.packages[this.getRandomInt(0, this.packages.length)];
      if (rand) {
        this.category_image = rand.server.icon;
      } else {
        console.log("as");
      }
    },
    getRandomInt: function(min, max) {
      return Math.floor(Math.random() * (max - min + 1)) + min;
    }
  }
};
</script>

<style>
</style>
