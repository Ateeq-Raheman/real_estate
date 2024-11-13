// Copyright (c) 2024, ateeq' and contributors
// For license information, please see license.txt

// frappe.ui.form.on("property", {
// 	refresh(frm) {

// 	},
// });
// Copyright (c) 2024, Ateeq and contributors
// For license information, please see license.txt

frappe.ui.form.on('property', {
    // setup: function (frm) {
    //     // check amenities duplicate
    //     frm.check_amenities_duplicate = function (frm, row) {
    //         frm.doc.amenities.forEach(item => {
    //             if (row.amenity == '' || row.idx == item.idx) {
    //                 // pass
    //             } else {
    //                 if (row.amenity == item.amenity) {
    //                     // clear field
    //                     row.amenity = '';
    //                     frappe.throw(__(`${item.amenity} already exists in row ${item.idx}`));
    //                     frm.refresh_field('amenities');
    //                 }
    //             }
    //         });
    //     };

    // // check flat against outdoor kitchen
    // frm.check_flat_against_outdoor_kitchen = function (frm, row) {
    //     if (row.amenity == "Outdoor Kitchen" && frm.doc.property_type == "Flat") {
    //         let amenity = row.amenity;
    //         row.amenity = '';
    //         frappe.throw(__(`${amenity} cannot exist in a flat`));
    //         frm.refresh_field('amenities');
    //     }
    // };
    // },

    // // refresh method to add custom buttons
    // refresh: function (frm) {
    //     // Add a custom button to say Hi
    //     frm.add_custom_button('Say Hi', () => {
    //         frappe.prompt('Address', ({ value }) => {
    //             if (value) {
    //                 frm.set_value('address', value);
    //                 frm.refresh_field('address');
    //                 frappe.msgprint(`Address field updated with ${value}`);
    //             }
    //         });
    //     }, "Actions");

    //     // Add a custom button to check property types
    //     frm.add_custom_button('Check Property Types', () => {
    //         let property_type = frm.doc.property_type;

    //         // Make ajax call to check property types
    //         frappe.call({
    //             method: "estate_app.estate_app.doctype.property.api.check_property_types",  // Update to the correct API method
    //             args: { 'property_type': property_type },
    //             callback: function (r) {
    //                 if (r.message.length > 0) {
    //                     let header = `<h3>Below properties are of type ${property_type}</h3>`;
    //                     let body = ``;
    //                     r.message.forEach(d => {
    //                         let cont = `<p>Name: ${d.name} - <a href='/desk#Form/Property/${d.name}'>View Property</a></p>`;
    //                         body += cont;
    //                     });
    //                     let all = header + body;
    //                     // Display the result in a message box
    //                     frappe.msgprint(__(all));
    //                 }
    //             }
    //         });
    //     }, "Actions");
    // },

    // // Property price field trigger
    // property_price: function (frm) {
    //     frm.compute_total(frm);
    // },

    // // Discount field trigger
    // discount: function (frm) {
    //     frm.copy_discount(frm);
    //     frm.compute_total(frm);
    // },
    map: function (frm) {
        let mapdata = JSON.parse(cur_frm.doc.map).features[0];
        if (mapdata && mapdata.geometry.type == "Point") {
            let lat = mapdata.geometry.coordinates[1];
            let long = mapdata.geometry.coordinates[0];
            console.log(lat, long);
            // make an API call
            frappe.call({
                type: "GET",
                url: `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${long}`,
                callback: function (r) {
                    // code snippet
                    console.log(r);
                    frm.set_value("address", r.display_name);
                }
            });
        }
    }
});

// Define the helper functions outside the form event
// Compute total function
// frm.compute_total = function (frm) {
//     let total = 0;
//     frm.doc.amenities.forEach(d => {
//         total += d.amenity_price;
//     });

//     let new_total = frm.doc.property_price + total;
//     if (frm.doc.discount) {
//         new_total -= (new_total * (frm.doc.discount / 100));
//     }

//     frm.set_value('grand_total', new_total);
// };

// // Copy discount to amenities
// frm.copy_discount = function (frm) {
//     frm.doc.amenities.forEach(d => {
//         d.discount = frm.doc.discount;
//     });
//     frm.refresh_field('amenities');
// };
