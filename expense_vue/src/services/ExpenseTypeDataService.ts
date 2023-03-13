import apiClient from "@/http-common";

class ExpenseTypeDataService {
    get(): Promise<any> {
        return apiClient.get(`/expensetypes`);
    }

    create(data: any): Promise<any> {
        return apiClient.post("/expensetypes", data);
    }

    update(id: any, data: any): Promise<any> {
        return apiClient.put(`/expensetypes/${id}`, data);
    }

    delete(id: any): Promise<any> {
        return apiClient.delete(`/expensetypes/${id}`);
    }

    //   findByName(name: string): Promise<any> {
    //     return apiClient.get(`/expensetypes?name=${name}`);
    //   }
}

export default new ExpenseTypeDataService();
