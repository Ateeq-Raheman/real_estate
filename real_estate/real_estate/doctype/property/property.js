// Copyright (c) 2021, Anthony Emmanuel (@Ghorz) and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {
    setup: function (frm) {
        frm.check_amenities_duplicate = function (frm, row) {
            frm.doc.amenities.forEach(item => {
                if (row.amenity == '' || row.idx == item.idx) {
                    // pass
                } else {
                    if (row.amenity == item.amenity) {
                        // clear field
                        row.amenity = '';
                        frappe.throw(`${item.amenity} already exists row ${item.idx}`);
                        frm.refresh_field('amenities');
                    }
                }
            });
        }

        frm.check_flat_against_outdoor_kitchen = function (frm, row) {
            if (row.amenity == "Outdoor Kitchen" && frm.doc.property_type == "Flat") {
                frappe.throw(`${row.amenity} cannot exist in a flat`);
                row.amenity = '';
                frm.refresh_field('amenities');
            }
        }
    },
    refresh: function (frm) {
        frm.add_custom_button('Say Hi', () => {
            frappe.prompt('Address', ({ value }) => {
                if (value) {
                    frm.set_value('address', value);
                    frm.refresh_field('address');
                    frappe.msgprint(__('Address field updated with ${value}'));
                }
            });
        });
    }
});


// AMENITIES CHILD TABLE
frappe.ui.form.on('Property Amenity Detail', {
    amenity: function (frm, cdt, cdn) {
        // grab the entire record
        let row = locals[cdt][cdn];
        frm.check_flat_against_outdoor_kitchen(frm, row);
        frm.check_amenities_duplicate(frm, row, row.amenity);
    }
});

