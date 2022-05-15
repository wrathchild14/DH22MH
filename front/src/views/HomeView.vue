<template>
  <v-main>
    <NavBar />
    <v-img
    class="mx-auto my-10"
          max-width="300"
          max-height="300"
          src="../assets/detective.jpg">

    </v-img>
    <v-row >
      <v-col cols="5">
        <v-card width="70%" class="mx-auto mt-10 elevation-0">
          <h1>filter i kategorizacija</h1>
        </v-card>
      </v-col>
      <v-col cols="7">
        <v-card width="70%" class="mx-auto mt-10 elevation-0">
          <v-file-input
            counter
            multiple
            show-size
            truncate-length="20"
            v-model="chosenFile"
            max-width="400"
          ></v-file-input>
          <div class="text-center my-10">
            <v-btn color="teal darken-4" class="white--text" rounded @click="Analyze()">Analyze data</v-btn>
          </div>
        </v-card>
      </v-col>
    </v-row>
    
     
    

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
