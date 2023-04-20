<template>
  <MainNavBar></MainNavBar>
  <div class="flex flex-col text-center w-full mb-12">
    <h1 class="sm:text-3xl text-2xl font-medium title-font mb-4 text-gray-900">
      FAQs
    </h1>
  </div>
  <section
    class="text-gray-600 body-font overflow-hidden"
    v-if="faqs.length > 0"
  >
    <div class="container px-5 py-24 mx-auto">
      <div class="-my-8 divide-y-2 divide-gray-100">
        <div
          class="py-8 flex flex-wrap md:flex-nowrap"
          v-for="faq in faqs"
          :key="faq.id"
        >
          <div class="md:w-64 md:mb-0 mb-6 flex-shrink-0 flex flex-col">
            <span class="font-semibold title-font text-gray-700"
              >Created at</span
            >
            <span class="mt-1 text-gray-500 text-sm">{{ faq.created_at }}</span>
          </div>
          <div class="md:flex-grow">
            <h2 class="text-2xl font-medium text-gray-900 title-font mb-2">
              {{ faq.subject }}
            </h2>
            <a
              class="text-indigo-500 inline-flex items-center mt-4"
              v-bind="{ href: '/viewFAQ/' + faq.id }"
              >More
              <svg
                class="w-4 h-4 ml-2"
                viewBox="0 0 24 24"
                stroke="currentColor"
                stroke-width="2"
                fill="none"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M5 12h14"></path>
                <path d="M12 5l7 7-7 7"></path>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
  <section v-else>No FAQs available</section>
</template>

<script>
import axios from "axios";
import MainNavBar from "@/components/MainNavbar.vue";
export default {
  components: { MainNavBar },
  name: "FaqView",
  data() {
    return {
      faqs: "",
    };
  },
  beforeCreate: [
    async function () {
      await axios
        .get("http://localhost:8000/api/tickets/faqs", {
          headers: {
            "Content-Type": "application/json",
            "Authentication-token": localStorage.getItem("token"),
          },
        })
        .then((response) => {
          this.faqs = response.data;
        })
        .catch((error) => {
          console.log(error.response.statusText);
        });
    },
  ],
};
</script>
