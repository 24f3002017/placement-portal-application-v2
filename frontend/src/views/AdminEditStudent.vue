<template>

    <div class="d-flex flex-column min-vh-100">
    
        <AdminNavbar/>
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                Edit Student
    
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            First Name
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.first_name"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Last Name
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.last_name"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Roll Number
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.roll_no"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Email
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.email"
                            disabled
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            CGPA
    
                        </label>
    
                        <input
                            type="number"
                            step="0.01"
                            class="form-control"
                            v-model="student.cgpa"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Education
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.education"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Skills
    
                        </label>
    
                        <input
                            class="form-control"
                            v-model="student.skills"
                        >
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Experience
    
                        </label>
    
                        <textarea
                            rows="4"
                            class="form-control"
                            v-model="student.experience"
                        ></textarea>
    
                    </div>
    
                    <div class="mb-3">
    
                        <label class="form-label">
    
                            Upload New Resume (PDF)
    
                        </label>
    
                        <input
                            type="file"
                            class="form-control"
                            accept=".pdf"
                            @change="handleResume"
                        >
    
                    </div>
    
                    <div class="text-center">
    
                        <button
                            class="btn btn-success me-2"
                            @click="updateStudent"
                        >
    
                            Save Changes
    
                        </button>
    
                        <button
                            class="btn btn-secondary"
                            @click="$router.back()"
                        >
    
                            Cancel
    
                        </button>
    
                    </div>
    
                </div>
    
            </div>
    
        </div>
    
    </div>
    
    </template>

<script setup>

import AdminNavbar from "../components/AdminNavbar.vue"

import { ref, onMounted } from "vue"

import { useRouter, useRoute } from "vue-router"

import axios from "axios"

const router = useRouter()

const route = useRoute()

const student = ref({})

const resume = ref(null)

function handleResume(event){

    resume.value = event.target.files[0]

}

async function fetchStudent(){

    try{

        const token = localStorage.getItem("token")

        const response = await axios.get(

            `http://127.0.0.1:5000/api/admin/student/${route.params.id}/edit`,

            {

                headers:{

                    Authorization:`Bearer ${token}`

                }

            }

        )

        student.value = response.data

    }

    catch(error){

        console.log(error.response)

    }

}

async function updateStudent(){

    try{

        const token = localStorage.getItem("token")

        const formData = new FormData()

        formData.append("first_name",student.value.first_name)

        formData.append("last_name",student.value.last_name)

        formData.append("roll_no",student.value.roll_no)

        formData.append("cgpa",student.value.cgpa)

        formData.append("education",student.value.education)

        formData.append("skills",student.value.skills)

        formData.append("experience",student.value.experience)

        if(resume.value){

            formData.append("resume",resume.value)

        }

        const response = await axios.put(

            `http://127.0.0.1:5000/api/admin/student/${route.params.id}/edit`,

            formData,

            {

                headers:{

                    Authorization:`Bearer ${token}`,

                    "Content-Type":"multipart/form-data"

                }

            }

        )

        alert(response.data.message)

        router.push(`/admin/student/${route.params.id}`)

    }

    catch(error){

        if(error.response){

            alert(error.response.data.message)

        }

        else{

            alert("Server Error")

        }

    }

}

onMounted(()=>{

    fetchStudent()

})

</script>