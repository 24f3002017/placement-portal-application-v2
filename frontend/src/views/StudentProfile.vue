<template>

    <div class="d-flex flex-column min-vh-100">
    
        <StudentNavbar/>
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                My Profile
    
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <table class="table">
    
                        <tbody>
    
                            <tr>
    
                                <th width="30%">Name</th>
    
                                <td>
    
                                    {{ student.first_name }}
                                    {{ student.last_name }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Roll Number</th>
    
                                <td>
    
                                    {{ student.roll_no }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Email</th>
    
                                <td>
    
                                    {{ student.email }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>CGPA</th>
    
                                <td>
    
                                    {{ student.cgpa }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Education</th>
    
                                <td>
    
                                    {{ student.education }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Skills</th>
    
                                <td>
    
                                    {{ student.skills }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Experience</th>
    
                                <td>
    
                                    {{ student.experience }}
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Resume</th>
    
                                <td>
    
                                    <a
    
                                        v-if="student.resume"
    
                                        :href="`http://127.0.0.1:5000/uploads/resumes/${student.resume}`"
    
                                        target="_blank"
    
                                        class="btn btn-primary btn-sm"
    
                                    >
    
                                        View Resume
    
                                    </a>
    
                                    <span
    
                                        v-else
    
                                        class="text-muted"
    
                                    >
    
                                        No Resume Uploaded
    
                                    </span>
    
                                </td>
    
                            </tr>
    
                        </tbody>
    
                    </table>
    
                    <div class="text-center mt-4">
    
                        <button
    
                            class="btn btn-warning me-2"
    
                            @click="$router.push('/student/profile/edit')"
    
                        >
    
                            Edit Profile
    
                        </button>
    
                        <button
    
                            class="btn btn-secondary"
    
                            @click="$router.back()"
    
                        >
    
                            Back
    
                        </button>
    
                    </div>
    
                </div>
    
            </div>
    
        </div>
    
    </div>
    
    </template>

<script setup>

import StudentNavbar from "../components/StudentNavbar.vue"

import { ref, onMounted } from "vue"

import { useRouter } from "vue-router"

import axios from "axios"

const router = useRouter()

const student = ref({})

async function fetchProfile() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            "http://127.0.0.1:5000/api/student/profile",

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        student.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

onMounted(() => {

    fetchProfile()

})

</script>