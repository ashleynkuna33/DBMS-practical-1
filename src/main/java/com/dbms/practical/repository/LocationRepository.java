package com.dbms.practical.repository;

import com.dbms.practical.entity.Location;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface LocationRepository extends JpaRepository<Location, Long> {
    Optional<Location> getLocationByName(String name);
}
