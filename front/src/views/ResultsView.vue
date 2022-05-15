<template>
  <v-main>
    <NavBar />
    <div class="projects">
      <v-container class="mt-5">
        <v-row>
          <v-col v-for="cv of this.cvs" :key="cv.name" md="4" xs="12">
            <v-card class="mx-auto my-10" max-width="344">
              <v-card-text>
                <div>Candidate</div>
                <p class="text-h4 text--primary">{{ cv.name }}</p>
                <p class="text-h8 text--primary">Categorization </p>
                <p>{{ cv.email }}</p>
                <p>{{ cv.address }}</p>
                <div class="text--primary">
                  {{ cv.faculty }}
                </div>
              </v-card-text>
              <v-card-text>
                <div class="font-weight-bold ml-8 mb-2">
                  Programming Languages
                </div>
                <v-timeline align-top dense>
                  <v-timeline-item
                    v-for="skill in cv.pr_lang"
                    :key="skill"
                    small
                  >
                    <div>
                      <div class="font-weight-normal">
                        <strong>{{ skill }}</strong>
                      </div>
                    </div>
                  </v-timeline-item>
                </v-timeline>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>
  </v-main>
</template>

<script>
import NavBar from "@/components/NavBar";
import { api } from "@/axios-api";

export default {
  data() {
    return {
      data: null,
      reveal: false,
      cvs: null,
      prediction: "",
      predicted: "",
    };
  },
  components: {
    NavBar,
  },
  methods: {
    getData() {
      api
        .get("api/get_info")
        .then((response) => {
          this.cvs = JSON.parse(response.data);
          // console.log(this.cvs);
          // for (let i = 0; i < this.cvs.length; i++) {
          //   const element = this.cvs[i];
          //   console.log(element);

          // }

          api.get("api/classify").then((res) => {
            this.prediction = JSON.parse(res.data);
            console.log(this.prediction[0].pred[0]);
            // this.predicted = this.prediction[0].pred[0]
          });
          for (const key of this.cvs) {
            console.log(key);
          }
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
  beforeMount() {
    this.getData();
  },
};
</script>
