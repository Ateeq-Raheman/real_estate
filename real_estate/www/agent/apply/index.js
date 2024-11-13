// $('#agent-form').on('submit', function (event) {
//     event.preventDefault();
//     makecall();
// });
// // Prevent default form submission

// let makecall = async () => {
//     // Serialize form data
//     let formdata = $(this).serializeArray().reduce(
//         (obj, item) => (obj[item.name] = item.value, obj), {}
//     );

//     console.log('Serialized Form Data:', formdata);

//     // Handling image data separately
//     let imagedata = $('#image')[0].files[0];
//     let imagefile = new FormData()
//     if (imagedata) {
//         imagefile.append('file', imagedata);
//         console.log('Image file selected:', imagedata.name);
//     } else {
//         console.log('No image selected');
//     }
//     // end intialize
//     // post to API
//     if (formdata) {
//         let res = await $.ajax({
//             url: '/api/resource/Agent',
//             type: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//                 'X-Frappe-CSRF-Token': frappe.csrf_token
//             },
//             data: JSON.stringify(formdata),
//             success: function (data) {
//                 return data
//                 console.log('Form submitted successfully:', data);
//             },
//             error: function (data) {
//                 console.log('Form submission failed:', data);
//             }
//         });
//         console.log(res);
//     }
// };


// // let makecall = async () => {
// //     let formdata = $('#agent-form').serializeArray().reduce(
// //         (obj, item) => (obj[item.name] = item.value, obj), {}
// //     );
// //     let imagedata = $('#image')[0].files[0];

// //     // initialize form
// //     let imagefile = new FormData();
// //     if (imagedata) {
// //         imagefile.append('file', imagedata);
// //     }
// //     // end initialize

// //     // post to API
// //     if (formdata) {
// //         let res = await $.ajax({
// //             url: '/api/resource/Agent',
// //             // Additional AJAX options (e.g., method, data) would go here
// //             type: "POST",
// //             type: 'POST',
// //             headers: {
// //                 'Content-Type': 'application/json',
// //                 'X-Frappe-CSRF-Token': frappe.csrf_token
// //             },
// //             data: JSON.stringify(formdata),// Convert formdata to JSON string 
// //             success: function (data) {
// //                 return data
// //             },
// //             error: function (data) {
// //                 return data
// //             }
// //         });
// //         console.log(res);
// //         // upload image
// //         if (res.data && imagedata) {
// //             let imgres = await fetch('/api/method/upload_file', {
// //                 headers: {
// //                     'X-Frappe-CSRF-Token': frappe.csrf_token
// //                 },
// //                 method: 'POST',
// //                 body: imagefile
// //             })
// //                 .then(res => res.json())
// //                 .then(data => {
// //                     console.log(data);
// //                 });
// //         }
// //     }
// // };

