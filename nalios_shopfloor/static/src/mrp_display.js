
    async selectWorkcenter(workcenterId, filterMO = false) {
        // Waits all the MO under validation are actually validated before to change the WC.
        const result = await this.processValidationStack();

        await this.useEmployee.getConnectedEmployees();

        if (result.success) {
            if (filterMO) {
                await this._onProductionBarcodeScanned(filterMO);
            } else {
                this.invalidateRecordIdsCache();
            }
            this.state.activeWorkcenter = Number(workcenterId);

            const employeeId = await this.useEmployee.getConnectedEmployees();
            await orm.call("mrp.workorder", "stop_employee", [workorderId, [employeeId]]);

            this.state.activeResModel = this.state.activeWorkcenter
                ? "mrp.workorder"
                : "mrp.production";
        }
    }