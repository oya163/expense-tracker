import apiClient from "@/http-common";

class ExpenseDataService {
    getAll(): Promise<any> {
        return apiClient.get("/expenses");
    }

    get(id: any): Promise<any> {
        return apiClient.get(`/expenses/${id}`);
    }

    create(data: any): Promise<any> {
        return apiClient.post("/expenses", data);
    }

    update(id: any, data: any): Promise<any> {
        return apiClient.put(`/expenses/${id}`, data);
    }

    delete(id: any): Promise<any> {
        return apiClient.delete(`/expenses/${id}`);
    }

    deleteAll(): Promise<any> {
        return apiClient.delete(`/expenses`);
    }

    //   findByName(name: string): Promise<any> {
    //     return apiClient.get(`/expenses?name=${name}`);
    //   }
}

export default new ExpenseDataService();
