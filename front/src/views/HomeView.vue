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

    <v-btn block @click="Analyze()">Analyze data</v-btn>

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
// import router from "@/router";
import { api } from "../axios-api";

export default {
  data: () => ({
    chosenFile: null,
    showAlert: false,
    dialog: false,
    fileData: null
  }),
  components: {
    NavBar,
  },
  methods: {
    Analyze() {
      if (!this.chosenFile) {
        this.showAlert = true;
      } else {
        console.log(this.chosenFile[0]);

        const form = new FormData()
        form.append('file', this.chosenFile[0])

        console.log(form);
        api
        .post("api/pdf", form)
        .then((response) => {
          console.log(response);
        })
        .catch((err) => {
          console.log(err);
        });
        // router.push("/results");
      }

    },
    processFile() {
    },
  },
};
</script>
