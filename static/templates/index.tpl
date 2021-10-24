<html>
    <head>
        <title>Via Web UI</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" integrity="sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A==" crossorigin=""/>
        <!-- Make sure you put this AFTER Leaflet's CSS -->
        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js" integrity="sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA==" crossorigin=""></script>

        <!-- SIDEBAR: -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">
        <link rel="stylesheet" href="static/resources/sidebar_menu.css">
        <!-- END SIDEBAR-->

    </head>

    <body>

        <!-- Sidebar from: https://www.codeply.com/p/1TlcDLPfiE -->
        <!-- Bootstrap row -->
        <div class="row" id="body-row">
            <!-- Sidebar -->
            <div id="sidebar-container" class="sidebar-expanded d-none d-md-block"><!-- d-* hiddens the Sidebar in smaller devices. Its itens can be kept on the Navbar 'Menu' -->

                <!-- Bootstrap List Group -->
                <ul class="list-group">
                    <!-- Logo
                    <li class="list-group-item logo-separator d-flex justify-content-center">
                        <img src='static/resources/logo.png' width="30" height="30" />
                    </li>
                     End Logo -->

                    <!-- Collapser -->
                    <a href="#" data-toggle="sidebar-colapse" class="bg-dark list-group-item list-group-item-action d-flex align-items-center">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span id="collapse-icon" class="fa fa-2x mr-3"></span>
                            <span id="collapse-text" class="menu-collapsed">Collapse</span>
                        </div>
                    </a>
                    <!-- End collapser -->

                    <!-- logo about link -->
                    <a href="#about-submenu" data-toggle="collapse" aria-expanded="false" class="bg-dark list-group-item list-group-item-action flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-fw mr-3">
                                 <img src='static/resources/logo.png' width="30" height="30" />
                            </span>
                            <span class="menu-collapsed">About</span>
                            <span class="submenu-icon ml-auto"></span>
                        </div>
                    </a>
                    <!-- Submenu content -->
                    <div id='about-submenu' class="collapse sidebar-submenu">
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white">
                           <div id="about_content_container">
                               <p>
                                  Via is a way to monitor road safety for cyclists.
                               </p>
                               <p>
                                  It has a strong emphasis on privacy, with no personally
                                  identifiable information being stored or transmitted, and
                                  all default options offering strong protections.
                                  For example, Via will not share the time of day, the
                                  beginning or end points of a journey or any means of
                                  linking one journey to another by default.
                               </p>
                               <p>
                                  If you want to help have a more transparent, complete
                                  coverage of cycling road quaity, you can download the
                                  app <a class="plain-link" style="display: inline" href="https://github.com/RobertLucey/via-app/releases/latest">here</a>.
                               </p>
                           </div>
                        </a>
                    </div>
                    <!-- End logo about link -->

                    <!-- Explore link -->
                    <a href="#submenu1" data-toggle="collapse" aria-expanded="false" class="bg-dark list-group-item list-group-item-action flex-column align-items-start">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-search fa-fw mr-3"></span>
                            <span class="menu-collapsed">Explore</span>
                            <span class="submenu-icon ml-auto"></span>
                        </div>
                    </a>
                    <!-- Submenu content -->
                    <div id='submenu1' class="collapse sidebar-submenu">
                        <a href="#" class="list-group-item list-group-item-action bg-dark text-white">
                           <div id="inputs_container">
                               <form id="pull_journeys_form">
                                   <!-- Time ranges: -->
                                   <label for="earliest_date">Earliest:</label>
                                   <input type="month" id="earliest_date" name="earliest_date" min="2021-01" value="2021-01">

                                   <label for="latest_date">Latest (inclusive):</label>
                                   <input type="month" id="latest_date" name="latest_date" max="2023-12" value="2023-12"><br/><br/>
                                   <!-- End time ranges -->

                                   <!-- Journey type: -->
                                   <input type="radio" id="all_journeys" name="journey_type" value="all">
                                   <label for="all">All Journeys</label><br>
                                   <input type="radio" checked="checked" id="bike" name="journey_type" value="bike">
                                   <label for="bike">Bike</label><br>
                                   <input type="radio" id="bus" name="journey_type" value="bus">
                                   <label for="bus">Bus</label><br>
                                   <input type="radio" id="car" name="journey_type" value="car">
                                   <label for="car">Car</label><br>
                                   <!-- End journey type -->

                                   <!-- Limit response:
                                   <label for="limit">Limit:</label>
                                   <input type="number" id="limit" name="limit" min="1" max="5000" value="10">
                                   End limit response -->

                                   <input type="submit" value="Submit">
                               </form>

                           </div>
                        </a>
                    </div>
                    <!-- End Explore link -->

                    <!-- Examples link -->
                    <a href="#" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-lightbulb-o fa-fw mr-3"></span>
                            <span class="menu-collapsed">Examples</span>
                        </div>
                    </a>
                    <!-- End Examples link -->

                    <!-- Twitter link -->
                    <a href="https://twitter.com/intent/tweet?text=Check%20out%20Via%20-%20It%27s%20visualizing%20road%20quality%20for%20cyclists%3A%20https%3A%2F%2Fviaroads.com" target="_blank" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-twitter fa-fw mr-3"></span>
                            <span class="menu-collapsed">Tweet</span>
                        </div>
                    </a>
                    <!-- End Twitter link -->

                    <!-- Contribute link -->
                    <a href="https://github.com/RobertLucey/via" class="bg-dark list-group-item list-group-item-action">
                        <div class="d-flex w-100 justify-content-start align-items-center">
                            <span class="fa fa-github fa-fw mr-3"></span>
                            <span class="menu-collapsed">Contribute</span>
                        </div>
                    </a>
                    <!-- End Contribute link -->

                </ul>
                <!-- List Group END-->

            </div><!-- sidebar-container END -->

            <!-- MAIN -->

            <div class="col" style="padding-right: 0; padding-left: 0">
                <div id="map_div" style="width: 100%; height: 100%"></div>
            </div><!-- Main Col END -->

        </div><!-- body-row END -->

        <script>
            function getColour(value){
                //value from 0 to 1
                var hue=((1-value)*120).toString(10);
                return ["hsl(",hue,",100%,50%)"].join("");
            }

            // This map is global scope.
            var map = L.map('map_div').setView({{initial_coords}}, {{initial_zoom}});
            // Public token from Mapbox is here. It can be left in, it's not secret.
            L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoicGhvbmVtYW4iLCJhIjoiY2tzazlwendiMDZ3NTJvcG50dzBlZDIzZCJ9.L0wR8vdrRgO4RQR6yLF6UA', {
                // Attribution must be left in for ToS reasons.
                attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
                maxZoom: 18,
                id: 'mapbox/streets-v11',
                tileSize: 512,
                zoomOffset: -1,
                accessToken: "REDACTED"
            }).addTo(map);

            // This is declared global scope so it can be deleted as needed.
            var geojson_layer = L.geoJson();

            function clear_geojson() {
                map.removeLayer(geojson_layer);
            }

            function load_geojson(data, clear_previous=false) {
                // Triggered on file upload with the GeoJSON object.
                if (clear_previous) {
                    clear_geojson();
                }

                geojson_layer = L.geoJSON(
                    data,
                    {
                        style: function(feature) {
                            return {
                                color: getColour(Math.max.apply(Math, [feature.properties.avg], 50) / 50),  // 50 is just a fairly high cap, TODO: get the actual height
                                weight: 5
                            };
                        },
                        onEachFeature: function(feature, layer) {
                            // A general method run on each feature. These bind popups for on
                            // layer click (default) and also on mouseover/out. Just the road
                            // name for now which isn't always populated.

                            layer.bindPopup(feature.properties.name + ": " + feature.properties.avg);

                            layer.on('mouseover', function(e) {
                                this.openPopup();
                            });
                            layer.on('mouseout', function(e) {
                                this.closePopup();
                            });
                        }
                    }
                )
                geojson_layer.addTo(map);
            }
        </script>

        <!-- Handle form submission etc -->
        <script>
            function update_map_from_form() {
                $.get(
                    'journeys/get_geojson',
                    {
                        'earliest_time': $('#earliest_date').val(),
                        'latest_time': $('#latest_date').val(),
                        'journey_type': $('input[name="journey_type"]:checked').val(),
                        'limit': $('#limit').val()
                    }
                ).done(function(resp) {
                    console.log("get_journeys response:")
                    console.log(resp);
                    load_geojson(resp, clear_previous=true);
                });
            }

            document.getElementById('pull_journeys_form').addEventListener('submit',
                function(e) {
                    e.preventDefault();
                    console.log("form submitted...");

                    update_map_from_form();
                }
            );

            // Call initially to have data show on map.
            update_map_from_form();
        </script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <script src="static/resources/sidebar_menu.js"></script>
    </body>
</html>
