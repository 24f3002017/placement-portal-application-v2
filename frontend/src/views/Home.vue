<template>

  <HomeNavbar />

  <!-- Hero Section -->
  <div
    style="position: relative; width: 100%; height: 500px; overflow: hidden;"
  >

    <img
      :src="iitImage"
      alt="IIT Madras"
      style="width:100%; height:100%; object-fit:cover;"
    >

    <div
      style="position:absolute;
             top:0;
             left:0;
             width:100%;
             height:100%;
             background:rgba(0,0,0,0.5);">
    </div>

    <div
      style="position:absolute;
             top:10%;
             left:5%;
             transform:translateY(-50%);
             color:white;">

      <h1
        style="font-size:3rem;
               font-weight:bold;
               margin-bottom:10px;">

        Welcome to the IIT Madras Placement Portal

      </h1>

    </div>

  </div>

  <!-- About -->

  <div
    style="max-width:900px;
           margin:60px auto;
           padding:0 20px;
           text-align:center;">

    <span
      style="border:1px solid grey;
             border-radius:20px;
             padding:5px 18px;
             font-size:0.85rem;
             color:grey;">

      ABOUT

    </span>

    <h2
      style="font-size:2.2rem;
             font-weight:bold;
             margin:20px 0 5px;">

      Know More About What We Are

    </h2>

    <h4
      style="font-size:1.2rem;
             font-weight:bold;
             margin-bottom:5px;">

      IIT Madras Placement Portal

    </h4>

    <p
      style="color:grey;
             margin-bottom:40px;">

      Connecting Excellence with Automated Efficiency

    </p>

    <h3
      style="font-size:1.6rem;
             font-weight:bold;
             margin-bottom:15px;">

      Streamlined Opportunities for Students and Recruiters

    </h3>

    <p
      style="color:grey;
             line-height:1.8;
             margin-bottom:25px;">

      The IIT Madras Placement Portal offers a seamless and fully automated
      operational process for both students and recruiters. This platform
      efficiently connects our students with leading job opportunities while
      providing recruiters with an automated and streamlined experience.
      Beyond traditional placement assistance, the portal actively collaborates
      with industries committed to making a significant impact. Our core focus
      remains on securing the best job opportunities for our students while
      contributing to the growth and development of the broader learning
      community.

    </p>

  </div>

  <!-- Placement Assistance -->

  <div
    style="text-align:center;
           padding:60px 20px;
           background-color:whitesmoke;">

    <h2
      style="font-size:2rem;
             font-weight:bold;
             margin-bottom:15px;">

      Our Placement Assistance

    </h2>

    <p
      style="color:black;
             font-size:1.1rem;
             max-width:700px;
             margin:0 auto;
             line-height:1.8;">

      We provide top-notch placement assistance to students enrolled in
      IIT Madras study programs and enable recruiters to identify and hire
      the most suitable candidates through a simple and efficient placement
      process.

    </p>

  </div>

</template>

<script setup>
import HomeNavbar from "../components/HomeNavbar.vue"
import iitImage from "../assets/IIT_madras.jpeg"
</script>