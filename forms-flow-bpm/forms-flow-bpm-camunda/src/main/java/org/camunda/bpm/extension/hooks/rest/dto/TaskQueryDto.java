package org.camunda.bpm.extension.hooks.rest.dto;

import java.util.List;

import org.camunda.bpm.engine.rest.dto.VariableQueryParameterDto;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

import lombok.Data;

@Data
@JsonIgnoreProperties(ignoreUnknown = true)
public class TaskQueryDto {

    private String name;
    private String tenant;
    private String status;
    private org.camunda.bpm.engine.rest.dto.task.TaskQueryDto criteria;
    private List<VariableQueryParameterDto> variables;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTenant() {
        return tenant;
    }

    public void setTenant(String tenant) {
        this.tenant = tenant;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }

    public org.camunda.bpm.engine.rest.dto.task.TaskQueryDto getCriteria() {
        return criteria;
    }

    public void setCriteria(org.camunda.bpm.engine.rest.dto.task.TaskQueryDto criteria) {
        this.criteria = criteria;
    }

    public List<VariableQueryParameterDto> getVariables() {
        return variables;
    }

    public void setVariables(List<VariableQueryParameterDto> variables) {
        this.variables = variables;
    }


}