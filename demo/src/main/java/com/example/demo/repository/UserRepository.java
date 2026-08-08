package com.example.demo.repository;

import com.example.demo.entity.AppUser;
import org.springframework.data.jpa.repository.JpaRepository;
import java.util.Optional;

public interface UserRepository extends JpaRepository<AppUser, Long> {
    // Spring Data JPA creates the query for you based on the method name!
    Optional<AppUser> findByUsername(String username);
}