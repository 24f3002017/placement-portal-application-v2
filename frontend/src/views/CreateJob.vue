<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar />
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
                Create Job
            </h2>
    
            <hr>
    
            <form @submit.prevent="createJob">
    
                <div class="mb-3">
    
                    <label class="form-label">Job Title</label>
    
                    <input
                        type="text"
                        class="form-control"
                        v-model="title"
                        required
                    >
    
                </div>
    
                <div class="mb-3">
    
                    <label class="form-label">Description</label>
    
                    <textarea
                        class="form-control"
                        rows="4"
                        v-model="description"
                        required
                    ></textarea>
    
                </div>
    
                <div class="mb-3">
    
                    <label class="form-label">Eligibility</label>
    
                    <input
                        type="text"
                        class="form-control"
                        v-model="eligibility"
                        required
                    >
    
                </div>
    
                <div class="mb-3">
    
                    <label class="form-label">Salary (Annual)</label>
    
                    <input
                        type="number"
                        class="form-control"
                        v-model="salary"
                        required
                    >
    
                </div>
    
                <div class="mb-3">
    
                    <label class="form-label">Skills Required</label>
    
                    <input
                        type="text"
                        class="form-control"
                        v-model="skills_req"
                        required
                    >
    
                </div>
    
                <div class="mb-3">
    
                    <label class="form-label">Experience Required (Years)</label>
    
                    <input
                        type="number"
                        class="form-control"
                        v-model="exp_req"
                        required
                    >
    
                </div>
    
                <div class="mb-4">
    
                    <label class="form-label">Application Deadline</label>
    
                    <input
                        type="date"
                        class="form-control"
                        v-model="deadline"
                        required
                    >
    
                </div>
    
                <button
                    class="btn btn-primary"
                    type="submit"
                >
                    Create Job
                </button>
    
            </form>
    
        </div>
    
    </div>
    
    </template>

<script setup>

import CompanyNavbar from "../components/CompanyNavbar.vue"
import { ref } from "vue"
import { useRouter } from "vue-router"
import axios from "axios"

const router = useRouter()

const title = ref("")
const description = ref("")
const eligibility = ref("")
const salary = ref("")
const skills_req = ref("")
const exp_req = ref("")
const deadline = ref("")

async function createJob() {

    try {

        const token = localStorage.getItem("token")

        await axios.post(

            "http://127.0.0.1:5000/api/company/job",

            {

                title: title.value,
                description: description.value,
                eligibility: eligibility.value,
                salary: salary.value,
                skills_req: skills_req.value,
                exp_req: exp_req.value,
                deadline: deadline.value

            },

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        alert("Job created successfully. Waiting for admin approval.")

        router.push("/company-dashboard")

    }

    catch(error) {

        console.log(error.response)

    }

}

</script>