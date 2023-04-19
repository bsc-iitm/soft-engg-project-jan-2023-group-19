<template>
  <div class="signup-container">
    <form class="signup-form" @submit.prevent="submitForm">
      <h2>Sign Up</h2>
      <div class="form-group">
        <label for="first_name">First Name:</label>
        <input type="text" id="first_name" v-model="firstName" required />
      </div>
      <div class="form-group">
        <label for="last_name">Last Name:</label>
        <input type="text" id="last_name" v-model="lastName" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div class="form-group">
        <label for="roll_number">Roll Number:</label>
        <input type="text" id="roll_number" v-model="rollNumber" required />
      </div>
      <div class="form-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Sign Up</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      firstName: "",
      lastName: "",
      email: "",
      rollNumber: "",
      password: "",
    };
  },
  methods: {
    submitForm() {
      axios
        .post(
          "http://localhost:8000/api/signup",
          {
            first_name: this.firstName,
            last_name: this.lastName,
            email: this.email,
            roll_number: this.rollNumber,
            password: this.password,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        )
        .then((response) => {
          alert(response.data.message);
          this.$router.push("/login");
        })
        .catch((error) => {
          alert(error.response.data.message);
        });
    },
  },
};
</script>

<style>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.signup-form {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff;
  padding: 30px;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
  display: flex;
  flex-direction: column;
  margin-bottom: 15px;
}

label {
  font-weight: bold;
  margin-bottom: 5px;
}

input {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #ccc;
  font-size: 16px;
  width: 100%;
}

button {
  padding: 10px;
  border-radius: 5px;
  border: none;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}
</style>
