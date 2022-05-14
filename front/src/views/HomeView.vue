<template>
  <v-main>
    <NavBar />
    <v-file-input
      counter
      multiple
      show-size
      truncate-length="20"
    ></v-file-input>
    <v-btn block to="results">Analyze data</v-btn>
  </v-main>
</template>

<script>
import NavBar from "@/components/NavBar";

export default {
  components: {
    NavBar,
  },
};
</script>
