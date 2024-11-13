frappe.pages['realestate-1'].on_page_load = function (wrapper) {
	new MyPage(wrapper);
}

// PAGE CONTENT 

MyPage = Class.extend({
	init: function (wrapper) {
		this.page = frappe.ui.make_app_page({
			parent: wrapper,
			title: 'real estate',
			single_column: true
		});
		// make page 
		this.make();
	},

	make: function () {
		// grab the class
		let me = $(this);

		// money formatter
		let currency = function (x) {
			let money = new Intl.NumberFormat('en-IN', {
				style: 'currency',
				currency: 'INR'
			}).format(x);

			return money;
		}



		//get total
		let total = function () {
			frappe.call({
				method: "real_estate.real_estate.page.realestate_1.realestate_1.get_total_price", //dotted path to server method
				callback: function (r) {
					// code snippet
					console.log(r);
					// set price data
					$("#total-price")[0].innerText = currency(r.message);
				}
			});
		}
		//GRAPH CALL
		let status = function () {
			frappe.call({
				method: "real_estate.real_estate.page.realestate_1.realestate_1.get_total_price", //dotted path to server method
				callback: function (r) {
					// code snippet
					console.log(r);
					let statuses = []
					let prices = []
					let message = r.message
					message.forEach((item) => {
						statuses.push(item[0])
						prices.push(item[1])
					});
					console.log(statuses, prices)
					// set price data
					// $("#total-price")[0].innerText = currency(r.message);

					///////////////////////////////////////////////
					// chart
					let page_chart = function () {
						const data = {
							labels: ["12am-3am", "3am-6pm", "6am-9am", "9am-12am",
								"12pm-3pm", "3pm-6pm", "6pm-9pm", "9am-12am"
							],
							datasets: [
								{
									name: "Some Data", type: "bar",
									values: [prices[0]]
								},
								{
									name: "Another Set", type: "line",
									values: [prices[1]]
								},
								{
									name: "Another Set", type: "line",
									values: [prices[2]]
								}
							]
						}

						let chart = new frappe.Chart("#chart", {  // or a DOM element,
							// new Chart() in case of ES6 module with above usage
							title: "My Awesome Chart",
							data: data,
							type: 'axis-mixed', // or 'bar', 'line', 'scatter', 'pie', 'percentage'
							height: 250,
							colors: ['#7cd6fd', '#743ee2']
						})
						console.log("ready")
						/////////////////////////////////////////////////////////////////////////////////////////
					}
				}
			})
		}




		// push dom element to the page
		$(frappe.render_template(frappe.realestate_1_page.body, this)).appendTo(this.page.main);
		// execute methods
		total();
		status();
		// refresh total
		document.querySelector("#refresh").addEventListener("click", () => {
			console.log("refresh button clicked");
			total();

		})


	}
	// end of the class


})

let body = `<div class="widget-group ">
				<div class="widget-group-head">
					
					<div class="widget-group-control"></div>
				</div>
				<div class="widget-group-body grid-col-3"><div class="widget number-widget-box" data-widget-name="Total Property Price">
			<div class="widget-head">
				<div class="widget-label">
					<div class="widget-title"><span class="ellipsis" title="Total Property Price">Total Property Price</span></div>
					<div class="widget-subtitle"></div>
				</div>
				<div class="widget-control"><div class="card-actions dropdown pull-right">
				<a data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				...
				</a>
				<ul class="dropdown-menu" style="max-height: 300px; overflow-y: auto;">
					<li class="dropdown-item">
									<a data-action="action-refresh" id="refresh">Refresh</a>
								</li><li class="dropdown-item">
									<a data-action="action-edit">Edit</a>
								</li>
				</ul>
			</div></div>
			</div>
			<div class="widget-body"><div class="widget-content">
			<div class="number" style="color: #29CD42;"  id="total-price">5000000</div>
			</div></div>
			<div class="widget-footer"></div>
		</div><div class="widget number-widget-box" data-widget-name="Total Absent (This Month)">
			<div class="widget-head">
				<div class="widget-label">
					<div class="widget-title"><span class="ellipsis" title="Total Absent (This Month)">Total Absent (This Month)</span></div>
					<div class="widget-subtitle"></div>
				</div>
				<div class="widget-control"><div class="card-actions dropdown pull-right">
				<a data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				...
				</a>
				<ul class="dropdown-menu" style="max-height: 300px; overflow-y: auto;">
					<li class="dropdown-item">
									<a data-action="action-refresh">Refresh</a>
								</li><li class="dropdown-item">
									<a data-action="action-edit">Edit</a>
								</li>
				</ul>
			</div></div>
			</div>
			<div class="widget-body"><div class="widget-content">
			<div class="number" style="color: #CB2929;">0</div>
			</div></div>
			<div class="widget-footer"></div>
		</div><div class="widget number-widget-box" data-widget-name="Late Entry (This Month)">
			<div class="widget-head">
				<div class="widget-label">
					<div class="widget-title"><span class="ellipsis" title="Late Entry (This Month)">Late Entry (This Month)</span></div>
					<div class="widget-subtitle"></div>
				</div>
				<div class="widget-control"><div class="card-actions dropdown pull-right">
				<a data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				...
				</a>
				<ul class="dropdown-menu" style="max-height: 300px; overflow-y: auto;">
					<li class="dropdown-item">
									<a data-action="action-refresh">Refresh</a>
								</li><li class="dropdown-item">
									<a data-action="action-edit">Edit</a>
								</li>
				</ul>
			</div></div>
			</div>
			<div class="widget-body"><div class="widget-content">
			<div class="number" style="color: #CB2929;">0</div>
			</div></div>
			<div class="widget-footer"></div>
		</div><div class="widget number-widget-box" data-widget-name="Early Exit (This Month)">
			<div class="widget-head">
				<div class="widget-label">
					<div class="widget-title"><span class="ellipsis" title="Early Exit (This Month)">Early Exit (This Month)</span></div>
					<div class="widget-subtitle"></div>
				</div>
				<div class="widget-control"><div class="card-actions dropdown pull-right">
				<a data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
				...
				</a>
				<ul class="dropdown-menu" style="max-height: 300px; overflow-y: auto;">
					<li class="dropdown-item">
									<a data-action="action-refresh">Refresh</a>
								</li><li class="dropdown-item">
									<a data-action="action-edit">Edit</a>
								</li>
				</ul>
			</div></div>
			</div>
			<div class="widget-body"><div class="widget-content">
			<div class="number" style="color: #CB2929;">0</div>
			</div></div>
			<div class="widget-footer"></div>
		</div></div>
			</div> 
			<div id="chart"></div>`;




// frappe.realestate_1 = {}

frappe.realestate_1_page = {
	body: body
}