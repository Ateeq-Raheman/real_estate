document.querySelector("#agent_button").addEventListener("click",
    (e) => {
        console.log("starting of the detail.js");

        let agent_email = document.querySelector("#email").value;
        let property_name = document.querySelector("#property-name").textContent;
        let d = new frappe.ui.Dialog({
            title: 'Enter details',
            fields: [
                {
                    label: 'Your Name',
                    fieldname: 'name',
                    fieldtype: 'Data'
                },
                {
                    label: 'Your email',
                    fieldname: 'email',
                    fieldtype: 'Data'
                },
                {
                    label: 'Message',
                    fieldname: 'message',
                    fieldtype: 'Small Text'
                }
            ],
            primary_action_label: 'Submit',
            primary_action(values) {
                console.log(values);
                console.log("Hi before the frappe call");
                // api call whitelist method
                frappe.call({
                    method: "real_estate.api.contact_agent", //dotted path to server method
                    args: values,
                    callback: function (r) {
                        // code snippet
                        console.log(r)
                        console.log("HI FROM the frappe call of DETAIL.JS")

                    }
                })
                d.hide();
            }
        });

        d.show();

    })

// document.querySelector("#agent_button").addEventListener("click", () => console.log("clicked"))
