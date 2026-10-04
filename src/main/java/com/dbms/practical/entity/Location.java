package com.dbms.practical.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.List;

@NoArgsConstructor
@AllArgsConstructor
@Entity
@Getter
@Setter
@Table(name = "location")
public class Location {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false)
    private String name;

    private String common_name;
    private String closest_building;

    @Column(nullable = false)
    private String directions;
    private String landmark;

    @OneToMany(mappedBy = "location")
    private List<Item> items;
}
