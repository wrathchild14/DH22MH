<template>
  <v-main>
    <NavBar />
     
    <v-file-input
      counter
      multiple
      show-size
      truncate-length="20"
      v-model="chosenFile"
      max-width="400"
    ></v-file-input>

    <div class="text-xs-center">
      <v-btn block @click="Analyze()">Analyze data</v-btn>
    </div>

    <v-dialog v-model="showAlert" width="210">
      <v-card>
        <v-card-title class="text-h10 red lighten-2">
          No files selected
        </v-card-title>
        <v-card-actions>
          <v-btn text @click="showAlert = false">Ok</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-main>
</template>

<script>
import NavBar from "@/components/NavBar";
import router from "@/router";

export default {
  data: () => ({
    chosenFile: null,
    showAlert: false,
    dialog: false,
  }),
  components: {
    NavBar,
  },
  methods: {
    Analyze() {
      if (!this.chosenFile) {
        this.showAlert = true;
      } else {
        console.log(this.chosenFile);
        router.push("/results");
      }
    },
  },
};
</script>
