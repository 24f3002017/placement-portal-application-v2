<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar />
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                Applicants
    
            </h2>
    
            <hr>
    
            <table class="table table-bordered">
    
                <thead>
    
                    <tr>
    
                        <th>SL</th>
                        <th>Student</th>
                        <th>Roll No</th>
                        <th>CGPA</th>
                        <th>Status</th>
                        <th>Action</th>
    
                    </tr>
    
                </thead>
    
                <tbody>
    
                    <tr
                        v-if="applicants.length==0"
                    >
    
                        <td
                            colspan="6"
                            class="text-center text-muted"
                        >
    
                            No applicants found.
    
                        </td>
    
                    </tr>
    
                    <tr
                        v-for="(applicant,index) in applicants"
                        :key="applicant.application_id"
                    >
    
                        <td>{{ index+1 }}</td>
    
                        <td>{{ applicant.name }}</td>
    
                        <td>{{ applicant.roll_no }}</td>
    
                        <td>{{ applicant.cgpa }}</td>
    
                        <td>{{ applicant.status }}</td>
    
                        <td>
    
                            <button
                                class="btn btn-primary btn-sm"
                                @click="viewApplicant(applicant.application_id)"
                            >
                                View Details
                            </button>
    
                        </td>
    
                    </tr>
    
                </tbody>
    
            </table>
    
            <button
                class="btn btn-secondary"
                @click="$router.back()"
            >
                Back
            </button>
    
        </div>
    
    </div>
    
    </template>

<script setup>

import CompanyNavbar from "../components/CompanyNavbar.vue"
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import axios from "axios"

const route = useRoute()
const router = useRouter()

const applicants = ref([])

async function fetchApplicants() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            `http://127.0.0.1:5000/api/company/job/${route.params.id}/applicants`,

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        console.log("Job ID:", route.params.id)
        console.log("Applicants:", response.data)

        applicants.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

function viewApplicant(applicationId) {

    router.push("/company/application/" + applicationId)

}

onMounted(() => {

    fetchApplicants()

})

</script>