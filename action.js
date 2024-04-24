// // function sendemail(){
 
// //    let data = document.querySelector("useremails");
// //    data.onc
// // }

// document.getElementById('sendemail').onclick = function(){
//    useremails =  document.getElementById('useremail').value;
//    usermessage = document.getElementById('usermessage').value;

// }

// console.log(useremails)

document.getElementById('sendemail').onclick = function() {
   let useremail = document.getElementById('useremails').value;
   let usermessage = document.getElementById('usermessage').value;

   console.log("User Email:", useremail);
   console.log("User Message:", usermessage);

   // Here you can add your email sending logic using the retrieved values
   // For example, you can use JavaScript to send an HTTP request to a server-side script that handles email sending.
   // Or you can use a service like EmailJS to send emails directly from the client-side.
};
