frappe.pages['database-console'].on_page_load = function (wrapper) {
	new MyPage(wrapper);
}

// PAGE CONTENT
MyPage = Class.extend({
	init: function (wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'Database Console',
			single_column: true
		});
		// make page
		this.make();
	},

	// make page
	make: function () {
		// grab the class
		let me = $(this);
		// form query 
		$(frappe.render_template(frappe.real_estate_page.body, this)).appendTo(this.page.main);
		const scriptTag = document.createElement('script');
		scriptTag.src = "https://unpkg.com/frappe-datatable@latest";
		scriptTag.type = "text/javascript";
		document.head.appendChild(scriptTag);
		function makeTable(data) {
			let datatable = new DataTable("#queryResult", {
				columns: data.tablehead,
				data: data.content,
				inlineFilters: true,
				dropdownButton: '▾',
			});
		}
		// get form data
		function makeQuery(formQuery) {
			// document.querySelector("#queryResult").innerText = formQuery;
			frappe.call({
				method: "real_estate.real_estate.page.database_console.database_console.query_database",
				args: { query: formQuery },
				callback: function (r) {
					// code snippet
					console.log(r);
					let el = $("#queryResult");
					let result = r.message;
					console.log(result);
					if (result.reply == 0) {
						frappe.throw(result.content);
					} else if (result.reply == 2) {
						el.addClass("text-danger");
						el[0].innerText = result.content;
					} else {
						if (result.content.length > 1) {
							makeTable(result);
						} else {
							frappe.msgprint("Empty Set");
						}

					}
				}
			});

		}


		$("#queryForm").submit(e => {
			e.preventDefault();
			let formquery = $("#query")[0].value;
			console.log(formquery);
			if (formquery.length > 1) {
				makeQuery(formquery);
			}
		})


	}
})
let body = ` 
			<div id = ""> 
			<form id="queryForm">
			<div class="form-group">
				<label for="query">Enter your sql query address</label>
				<textarea class="form-control" id="query" aria-describedby="query" placeholder="Enter query"></textarea>
				<small id="emailHelp" class="form-text text-muted">think before entering the data.</small>
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
			</form> 
			</div>
			<div id="queryResult" ></div>
			`;
frappe.real_estate_page = {
	body: body
}
