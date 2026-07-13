<template>

    <div class="d-flex flex-column min-vh-100">
    
        <CompanyNavbar />
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
                Job Details
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">
    
                    <table class="table">
    
                        <tbody>
    
                            <tr>
                                <th width="30%">Job Title</th>
                                <td>{{ job.title }}</td>
                            </tr>
    
                            <tr>
                                <th>Description</th>
                                <td>{{ job.description }}</td>
                            </tr>
    
                            <tr>
                                <th>Eligibility</th>
                                <td>{{ job.eligibility }}</td>
                            </tr>
    
                            <tr>
                                <th>Salary</th>
                                <td>{{ job.salary }}</td>
                            </tr>
    
                            <tr>
                                <th>Skills Required</th>
                                <td>{{ job.skills_req }}</td>
                            </tr>
    
                            <tr>
                                <th>Experience Required</th>
                                <td>{{ job.exp_req }} Years</td>
                            </tr>
    
                            <tr>
                                <th>Application Deadline</th>
                                <td>{{ job.deadline }}</td>
                            </tr>
    
                            <tr>
                                <th>Approval Status</th>
    
                                <td>
    
                                    <span
                                        class="badge bg-warning text-dark"
                                        v-if="job.approval_status=='pending'"
                                    >
                                        Pending
                                    </span>
    
                                    <span
                                        class="badge bg-success"
                                        v-if="job.approval_status=='approved'"
                                    >
                                        Approved
                                    </span>
    
                                    <span
                                        class="badge bg-danger"
                                        v-if="job.approval_status=='rejected'"
                                    >
                                        Rejected
                                    </span>
    
                                </td>
    
                            </tr>
    
                            <tr>
    
                                <th>Current Status</th>
    
                                <td>
    
                                    <span
                                        class="badge bg-success"
                                        v-if="job.status=='active'"
                                    >
                                        Active
                                    </span>
    
                                    <span
                                        class="badge bg-secondary"
                                        v-else
                                    >
                                        Inactive
                                    </span>
    
                                </td>
    
                            </tr>
    
                            <tr>
                                <th>Total Applicants</th>
                                <td>{{ job.applicants }}</td>
                            </tr>
    
                        </tbody>
    
                    </table>
    
                    <div class="text-center mt-4">
    
                        <button class="btn btn-success me-2"
                        v-if="job.status == 'inactive' && job.approval_status == 'approved'"
                        @click="changeStatus">
                        Activate Job
                    </button>
                    
                    <button
                    class="btn btn-warning me-2"
                    v-if="job.status == 'active'"
                    @click="changeStatus">
                    Close Job
                </button>
                
                <button 
                class="btn btn-info me-2"
                @click="viewApplications">
                View Applicants
            </button>
    
                    </div>
    
                    <div class="text-center mt-4">
    
                        <button
                            class="btn btn-secondary"
                            @click="$router.push('/company-dashboard')"
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

import CompanyNavbar from "../components/CompanyNavbar.vue"
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import axios from "axios"

const route = useRoute()
const router = useRouter()

const job = ref({})

async function fetchJob() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            `http://127.0.0.1:5000/api/company/job/${route.params.id}`,

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        job.value = response.data

    }

    catch(error) {

        console.log(error.response)

    }

}

async function changeStatus() {

    try {

        const token = localStorage.getItem("token")

        await axios.put(

            `http://127.0.0.1:5000/api/company/job/${route.params.id}/status`,

            {},

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        alert("Job status updated successfully.")

        fetchJob()

    }

    catch(error) {

        console.log(error.response)

        alert(error.response?.data?.message || "Something went wrong.")

    }

}

function viewApplications() {

router.push(
    "/company/job/" + route.params.id + "/applications"
)

}

onMounted(() => {

    fetchJob()

})

</script>