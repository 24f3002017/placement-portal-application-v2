<template>
  <HomeNavbar />
  <div class="container mt-5 flex-grow-1">

    <div class="row justify-content-center">

      <div class="col-md-7">

        <div class="card shadow">

          <div class="card-body">

            <h2 class="text-center mb-4">
              Student Registration
            </h2>

            <div class="mb-3">
              <label class="form-label">Email</label>
              <input
                type="email"
                class="form-control"
                v-model="email"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Password</label>
              <input
                type="password"
                class="form-control"
                v-model="password"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Roll Number</label>
              <input
                type="text"
                class="form-control"
                v-model="roll_no"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">First Name</label>
              <input
                type="text"
                class="form-control"
                v-model="first_name"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Last Name</label>
              <input
                type="text"
                class="form-control"
                v-model="last_name"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Skills</label>
              <input
                type="text"
                class="form-control"
                v-model="skills"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">CGPA</label>
              <input
                type="number"
                step="0.01"
                class="form-control"
                v-model="cgpa"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Experience</label>
              <textarea
                class="form-control"
                v-model="experience"
              ></textarea>
            </div>

            <div class="mb-3">
              <label class="form-label">Resume (PDF)</label>
              <input
                type="file"
                class="form-control"
                accept=".pdf"
                @change="handleResumeUpload"
              >
            </div>

            <div class="mb-3">
              <label class="form-label">Education</label>
              <input
                type="text"
                class="form-control"
                v-model="education"
              >
            </div>

            <button
              class="btn btn-success w-100"
              @click="registerStudent"
            >
              Register
            </button>

            <p class="text-danger mt-3">
              {{ message }}
            </p>

          </div>

        </div>

      </div>

    </div>

  </div>
</template>

<script setup>

import HomeNavbar from "../components/HomeNavbar.vue"
import { ref } from "vue"
import axios from "axios"
import { useRouter } from "vue-router"

const router = useRouter()

const email = ref("")
const password = ref("")
const roll_no = ref("")
const first_name = ref("")
const last_name = ref("")
const skills = ref("")
const cgpa = ref("")
const experience = ref("")
const education = ref("")
const resume = ref(null)
const message = ref("")

function handleResumeUpload(event) {
    resume.value = event.target.files[0]
    console.log("Selected file:", resume.value)
}

async function registerStudent() {

  try {

    const formData = new FormData()

    formData.append("email", email.value)

    formData.append("password", password.value)

    formData.append("roll_no", roll_no.value)

    formData.append("first_name", first_name.value)

    formData.append("last_name", last_name.value)

    formData.append("skills", skills.value)

    formData.append("cgpa", cgpa.value)

    formData.append("experience", experience.value)

    formData.append("education", education.value)

    if (resume.value) {

formData.append("resume", resume.value)

}

const response = await axios.post(

"http://127.0.0.1:5000/api/student/register",

formData,

{

  headers: {

    "Content-Type": "multipart/form-data"

  }

}

)

alert(response.data.message)

router.push("/login")

}

catch(error) {

if (error.response) {

message.value = error.response.data.message

}

else {

message.value = "Server error"

}

}

}

</script>