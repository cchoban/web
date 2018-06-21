<template>
    <div class="terminal">
        <p>C:\> chob -S {{ packagename }}</p>
    </div>
</template>


<style lang="scss" scoped>
.terminal {
  width: 300px;
  height: 60px;
  color: #fff;
  background-color: #2a303b;
  border-radius: 5px;
  border: 5px solid #ccc;

  p {
    margin-top: 14px;
    margin-left: 15px;
  }
}
</style>

<script>
export default {
  props: ["packagename"]
};
</script>

