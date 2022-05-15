<template>
  <v-main>
    <NavBar />
    <v-card flat>
      <v-row>
        <v-col>
          <v-card flat class="d-flex align-start mx-10">
            <v-img
              class="mx-auto my-10"
              max-width="200"
              max-height="200"
              src="../assets/dragonhack_logo.jpeg"
            >
            </v-img>
          </v-card>
        </v-col>
        <v-col>
          <v-card class="d-flex align-start mx-10" flat tile>
            <v-img
              class="mx-auto my-10"
              max-width="200"
              max-height="200"
              src="../assets/paper.png"
            >
            </v-img>
          </v-card>
        </v-col>
      </v-row>
    </v-card>

    <v-row>
      <v-col cols="5">
        <v-card width="70%" class="mx-auto mt-10 elevation-0">
          <h4 style="font-family: 'Verdana'">Filters</h4>
          <v-container>
            <v-checkbox
              v-model="showCategorization"
              label="Categorization"
              value="Categorization"
            >
              Categorization
            </v-checkbox>
          </v-container>
          <v-text-field dense outlined label="Keywords"></v-text-field>

          <v-text-field
            solo
            label="Location"
            append-outer-icon="mdi-map-marker"
          ></v-text-field>

          <v-text-field
            v-model="yearsExperience"
            label="Minimum years of experience"
            value="1"
            suffix="years"
          ></v-text-field>
        </v-card>
      </v-col>
      <v-col cols="7">
        <v-card width="70%" class="mx-auto mt-10 elevation-0">
          <h4 style="font-family: 'Verdana'">Attach files below</h4>
          <v-file-input
            counter
            multiple
            show-size
            truncate-length="20"
            v-model="chosenFile"
            max-width="400"
            class="my-10"
          ></v-file-input>
          <div class="text-center my-10">
            <v-btn
              color="blue darken-3"
              class="white--text"
              x-large
              rounded
              @click="Analyze()"
              >Analyze data</v-btn
            >
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
    fileData: null,
  }),
  components: {
    NavBar,
  },
  methods: {
    Analyze() {
      if (!this.chosenFile) {
        this.showAlert = true;
      } else {
        api.get("api/del_pdf").then(() => {
          console.log("Deleted pdfs and created fresh pdf");

          // const form = new FormData();
          // form.append("file", this.chosenFile[0]);
          // api
          //   .post("api/pdf", form)
          //   .then((response) => {
          //     console.log(response);
          //   })
          //   .catch((err) => {
          //     console.log(err);
          //   });

          for (const file of this.chosenFile) {
            const form = new FormData();
            form.append("file", file);
            fetch("http://127.0.0.1:8000/api/pdf", {
              method: "POST",
              body: form,
            }).then((res) => {
              console.log("Request complete! response:", res);
            });
          }

          // router.push("/results");

        });
      }
    },
    processFile() {},
  },
};
</script>
