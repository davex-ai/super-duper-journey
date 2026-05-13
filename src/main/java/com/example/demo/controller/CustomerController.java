package com.example.demo.controller;

import com.example.demo.entity.Customer;
import com.example.demo.service.CustomerService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/customers")
public class CustomerController{

    @Autowired
    private CustomerService customerService;

    @GetMapping("/{id}")
    public Customer getCustomerById(@PathVariable Long id){ return customerService.getCustomerById(id);}
    @GetMapping() public List<Customer> getCustomers(){ return customerService.getCustomers();}

    @PostMapping
    public Customer createCustomer(@RequestBody Customer customer){ return customerService.createCustomer(customer);}


    @DeleteMapping("/{id}")
    public String deleteCustomer(@PathVariable Long id){ customerService.deleteCustomer(id); return "Customer deleted successfully";}

    @PutMapping("/{id}")
    public Customer updateCustomer(@PathVariable Long id, @RequestBody Customer customer){
        return customerService.updateCustomer(id, customer);
    }
}

