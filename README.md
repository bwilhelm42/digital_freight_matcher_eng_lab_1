# Engineering Lab 1 - Digital Freight Matching

## Problem Statement
<p>Infinity and Beyond, a family-owned trucking enterprise based in Atlanta, GA, recently landed a significant contract with the Too-Big-To-Fail company. This substantial collaboration led them to acquire five new trucks and establish expansive routes spanning the entirety of the state. Despite having fixed rates determined by the volume of cargo transported, the company faces challenges. The mounting pressures of inflation and decreased contracted cargo have caused them to feel the financial pinch on some of these routes.</p>
<p>The dilemma deepens when considering their binding four-year contract that prevents them from canceling any existing routes. This contractual commitment, coupled with the specialized trucks they've already invested in for the project, has placed them in a tight spot. The repercussions of prematurely terminating the contract would involve hefty fines, and the ongoing maintenance of the trucks only adds to their predicament.</p>
<p>In search of a solution, the owners of Infinity and Beyond, Mr. and Miss. Lightyear stumbled upon news about Digital Freight Matching (DFM). Investing their weekend into comprehending this concept, they began to see it as a potential lifeline for their company's current challenges.</p>

## Solution

<p>Build a Pricing and Scheduling Service that allows Mr. and Miss. Lightyear to offer cargo space in the current fixed routes, to clients that want to transport through those same paths. The service will receive orders in a specific format (used in their current control system), and will try to match any existing route, based on the following criteria:</p>

- Pick up and drop off locations must be at most  at a distance of 1 km of any point inside any preexisting routes.
- Cargo (set of packages) must fill in the truck's compartment (taking into account the original cargo, and all cargo being included on it).
- Every pick up and drop off takes 15 minutes, plus deviation from the route (up to 1km from any preexisting point).
- All costs per mile involved are given by a spreadsheet that's updated by Mr. Lightyear.
- Cargo that can't fit on any route, can be saved and combined with other clients' cargo, to form a new route. New routes MUST be profitable.
- Routes must go back to the point of origin, and can't last longer than 10 hours/day.

**BONUS**:
- Includes cargo type: Some types can't be transported together;
- Union: Truck drivers must take a 30 minute break after 4 hours of work.

## Overall Architecture

![architecture](/assets/architecture.png)

### Order format (received by the Service)

```	
{
	cargo: {
		    "packages": [1, 60, 'standard'] // CBM (vol.), weight (pounds), type
    },
	pick-up: {
		    "latitude": 33.754413815792205, 
		    "longitude": -84.3875298776525
    },
    drop-off: {
		    "latitude": 34.87433824316913, 
		    "longitude": -85.08447506395166
    }
}
```

### Route format

```
route: [
	{
        "latitude": 33.754413815792205, 
		"longitude": -84.3875298776525    // <- Starting Point
    },
    {
	    "latitude": 34.87433823445323, 
		"longitude": -85.084123334995166
    },
    {
	    "latitude": 34.87433823445323, 
		"longitude": -85.084123334995166
    },
    {
	    "latitude": 34.87433824316913, 
		"longitude": -85.08447506395166
    },
	{
        "latitude": 33.754413815792205, 
		"longitude": -84.3875298776525 // <- Last Point
    }
]
```

### Current Routes

![routes](/assets/existing_routes.png)

## Docker Setup

This setup allows hot reloading of the code.
Depending on your setup you may need to run the docker commands with `sudo`.

1. Install Docker and docker-compose
	- Install docker-buildx if you don't have docker desktop installed

2. Navigate to the project directory. In the docker-compose.yml file, set the target as development or production accordingly

3. Build the docker compose image

	```sh
	docker compose up
	```

4. Open the browser and go to http://localhost:8000

## VirtEnv Setup

1. Install Python 3.10

	```sh
	brew install python@3.10
	```

1. Install venv

	```sh
	pip install venv
	```

1. Create a virtual environment

	```sh
	python -m venv venv
	```

1. Activate the virtual environment

	```sh
	source venv/bin/activate
	```

1. Install the dependencies

	```sh
	pip install -r requirements.txt
	```

1. Run the project

	```sh
	uvicorn main:app --host 0.0.0.0 --port 8080 --reload
	```

1. Open the browser and go to http://localhost:8080

## References

### Trucking information

- <a href="https://convoy.com/digital-freight-network/">Digital Freight Network</a>
- <a href="https://www.freightcourse.com/digital-freight-matching/">DFM - Digital Freight Matching</a>
- <a href="https://www.inboundlogistics.com/articles/deadhead-trucking/#:~:text=Deadhead%20trucking%20is%20when%20a,and%20how%20to%20minimize%20it">Deadhead Trucking.</a>
- <a href="https://www.truckinfo.net/research/trucking-statistics">Trucking Trends</a>

### Project documentation

- [Eng. Labs 1 - Digital Freight Matching](https://docs.google.com/spreadsheets/d/1cSc2ZNoU0yKbgvMdWE2HC2mP214_PApjAlzfwvX_KUs/edit#gid=0)
- [Digital Freight Matching project google doc](https://docs.google.com/document/d/1mUVKYH44ZExaQzY1FqbnZCXabasc_k3vlqs3n3qKqg4/edit?pli=1#heading=h.8g5sf6ejx8q6)
- [project board](https://github.com/users/bwilhelm42/projects/1/views/1)

<span><i>Made at <a href='https://qwasar.io'>Qwasar Silicon Valley</a></i></span> <span><img alt='Qwasar Silicon Valley Logo' src='https://storage.googleapis.com/qwasar-public/qwasar-logo_50x50.png' width='20px'></span>
