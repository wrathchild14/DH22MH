<template>
  <v-main>
    <NavBar />
    <v-card class="mx-auto my-10" max-width="344">
      <v-card-text>
        <div>Candidate</div>
        <p class="text-h4 text--primary">{{ data.name }}</p>
        <p>{{ data.email }}</p>
        <div class="text--primary">
          {{ data.faculty }}
        </div>
      </v-card-text>
      <v-card-text>
        <div class="font-weight-bold ml-8 mb-2">Programming Languages</div>
        <v-timeline align-top dense>
          <v-timeline-item v-for="skill in data.pr_lang" :key="skill" small>
            <div>
              <div class="font-weight-normal">
                <strong>{{ skill }}</strong>
              </div>
            </div>
          </v-timeline-item>
        </v-timeline>
      </v-card-text>
    </v-card>
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
          this.data = JSON.parse(response.data);
          console.log(this.data);
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
