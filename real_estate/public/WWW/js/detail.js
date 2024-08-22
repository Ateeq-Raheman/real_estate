document.querySelector("#contact-agent").addEventListener("click",
    (e) => {
        console.log("ehdiuwdeiuhwdwd");

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
                // api call whitelist method
                frappe.call({
                    method: "real_estate.api.contact_agent", //dotted path to server method
                    args: values,
                    callback: function (r) {
                        // code snippet
                        console.log('hiiiiiiiiiiiiiiiii')

                    }
                })
                d.hide();
            }
        });

        d.show();

    })