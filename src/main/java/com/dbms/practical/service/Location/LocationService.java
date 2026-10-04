package com.dbms.practical.service.Location;

import com.dbms.practical.dto.LocationRequest;
import com.dbms.practical.entity.Location;
import com.dbms.practical.repository.LocationRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class LocationService implements ILocation{
    private final LocationRepository locationRepository;

    @Override
    public List<Location> getLocations() {
        return locationRepository.findAll();
    };
    @Override
    public Location getLocationById(Long id) {
        return locationRepository.findById(id);
    };
    @Override
    public Location getLocationByName(String name) {
        return locationRepository.getLocationByName(name);
    };
    @Override
    public Location createLocation(Long user_id, LocationRequest request) {
        return null;
    };
    @Override
    public Location removeLocation(Long id) {
        return null;
    };
    @Override
    public Location updateLocation(Long id, LocationRequest request) {
        return null;
    };

}
