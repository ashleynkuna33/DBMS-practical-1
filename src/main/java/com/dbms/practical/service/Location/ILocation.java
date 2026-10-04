package com.dbms.practical.service.Location;

import com.dbms.practical.dto.LocationRequest;
import com.dbms.practical.entity.Location;

import java.util.List;

public interface ILocation {
    // for this entity we cant to get the location, create, update
    List<Location> getLocations();
    Location getLocationById(Long id);
    Location getLocationByName(String name);
    Location createLocation(Long user_id, LocationRequest request);
    Location removeLocation(Long id);
    Location updateLocation(Long id, LocationRequest request);
}
