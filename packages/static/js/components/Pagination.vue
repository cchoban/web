<template>
    <div aria-label="Pagination Navigation" role="navigation" class="ui pagination pointing secondary menu">
  <a class="item" v-if="packages.previous != null" @click="getPackages(previousUrl)">⟨</a>
  <a class="item" v-for="(num, pages) in countPageNumber" @click="getPackages('http://localhost:8000/api/packages/?limit=10&offset='+num)">{{ pages }}</a>
  <a class="item" v-if="packages.next != null" @click="getPackages(nextUrl)">⟩</a>
</div>

</template>

<script>
export default {

}
</script>

<style>

</style>
