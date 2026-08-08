package com.example.demo.service;

import com.example.demo.entity.Customer;
import com.example.demo.repository.CustomerRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CustomerService{
    @Autowired
    private CustomerRepository customerRepository;

    public Customer getCustomerById(Long id){return customerRepository.findById(id).orElseThrow(() -> new RuntimeException("Not Fouund"));}
    public Customer createCustomer(Customer customer){return customerRepository.save(customer);}
    public void deleteCustomer(Long id){ customerRepository.deleteById(id);}
    public Customer updateCustomer(Long id, Customer updatedCustomer){
        Customer existing = customerRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Customer not found"));

        existing.setName(updatedCustomer.getName());
        existing.setEmail(updatedCustomer.getEmail());

        return customerRepository.save(existing);
    }

    public List<Customer> getCustomers() {
        return customerRepository.findAll();
    }
}


