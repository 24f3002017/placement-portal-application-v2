    <template>
    
    <div class="d-flex flex-column min-vh-100">
    
        <StudentNavbar/>
    
        <div class="container my-5 flex-grow-1">
    
            <h2 class="text-center mb-4">
    
                Job Details
    
            </h2>
    
            <div class="card shadow">
    
                <div class="card-body">

                    <div
    class="alert alert-success"
    v-if="job.status=='selected'"
>

    <h5>🎉 Congratulations!</h5>

    <p class="mb-0">

        You have been selected by
        <strong>{{ job.company }}</strong>.

    </p>

</div>
    
                    <table class="table">
    
                        <tbody>
    
                            <tr>
                                <th width="30%">Company</th>
                                <td>{{ job.company }}</td>
                            </tr>
    
                            <tr>
                                <th>Position</th>
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
                                <td>{{ job.skills_required }}</td>
                            </tr>
    
                            <tr>
                                <th>Experience Required</th>
                                <td>{{ job.experience_required }}</td>
                            </tr>
    
                            <tr>
                                <th>Deadline</th>
                                <td>{{ job.deadline }}</td>
                            </tr>

                            <tr v-if="job.package">

<th>Package Offered</th>

<td>

    {{ job.package }} LPA

</td>

</tr>

<tr v-if="job.offer_letter">

<th>Offer Letter</th>

<td>

    <a

        :href="`http://127.0.0.1:5000/uploads/offers/${job.offer_letter}`"

        target="_blank"

        class="btn btn-success btn-sm"

    >

        Download Offer Letter

    </a>

</td>

</tr>
    
                        </tbody>
    
                    </table>
    
                    <div
                        class="card mt-4"
                        v-if="job.already_applied"
                    >
    
                        <div class="card-header">
    
                            <h5 class="mb-0">
    
                                Application Status
    
                            </h5>
    
                        </div>
    
                        <div class="card-body">
    
                            <table class="table mb-0">
    
                                <tbody>
    
                                    <tr>
                                        <th width="30%">Status</th>
    
                                        <td>
    
                                            <span
    class="badge bg-success"
    v-if="job.status=='selected'"
>
    Selected
</span>

<span
    class="badge bg-warning text-dark"
    v-else-if="job.status=='shortlisted'"
>
    Shortlisted
</span>

<span
    class="badge bg-danger"
    v-else-if="job.status=='rejected'"
>
    Rejected
</span>

<span
    class="badge bg-primary"
    v-else
>
    {{ job.status }}
</span>
    
                                        </td>
    
                                    </tr>
    
                                    <tr>
    
                                        <th>Feedback</th>
    
                                        <td>
    
                                            {{ job.feedback || "No feedback available." }}
    
                                        </td>
    
                                    </tr>
    
                                    <tr v-if="job.interview_date">
    
                                        <th>Interview Date</th>
    
                                        <td>{{ job.interview_date }}</td>
    
                                    </tr>
    
                                    <tr v-if="job.interview_time">
    
                                        <th>Interview Time</th>
    
                                        <td>{{ job.interview_time }}</td>
    
                                    </tr>
    
                                    <tr v-if="job.interview_mode">
    
                                        <th>Interview Mode</th>
    
                                        <td>{{ job.interview_mode }}</td>
    
                                    </tr>
    
                                    <tr v-if="job.interview_location">
    
                                        <th>Meeting Link / Location</th>
    
                                        <td>{{ job.interview_location }}</td>
    
                                    </tr>
    
                                </tbody>
    
                            </table>
    
                        </div>
    
                    </div>
    
                    <div class="text-center mt-4">
    
                        <button
    
                            v-if="!job.already_applied"
    
                            class="btn btn-success me-2"
    
                            @click="applyJob"
    
                        >
    
                            Apply Now
    
                        </button>
    
                        <button
    
                            v-else
    
                            class="btn btn-secondary me-2"
    
                            disabled
    
                        >
    
                        {{ job.status=="selected" ? "Selected" : "Already Applied" }}
    
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

import { useRoute } from "vue-router"

import axios from "axios"

const route = useRoute()

const job = ref({})

async function fetchJob() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.get(

            `http://127.0.0.1:5000/api/student/job/${route.params.id}`,

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

async function applyJob() {

    try {

        const token = localStorage.getItem("token")

        const response = await axios.post(

            `http://127.0.0.1:5000/api/student/job/${route.params.id}/apply`,

            {},

            {

                headers: {

                    Authorization: `Bearer ${token}`

                }

            }

        )

        alert(response.data.message)

        fetchJob()

    }

    catch(error) {

        if(error.response){

            alert(error.response.data.message)

        }

        else{

            alert("Server Error")

        }

    }

}

onMounted(() => {

    fetchJob()

})

</script>