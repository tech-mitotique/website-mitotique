@description('Environment to deploy the resourecs')
@allowed([
  'dev'
  'prod'
])
param environment string

@description('The azure region which the resource should be deployed to. Defaults to resource group\'s location')
param resourceLocation string = resourceGroup().location

// @description('A suffix string to make resource names unique. Defaults to autogenerated string using resource group\'s id.')
// @maxLength(13)
// param resourceNameSuffix string = uniqueString(resourceGroup().id)

var appServicePlanName = 'website-mitotique-plan-${environment}'
// var appServiceAppName = 'website-mitotique-app-${environment}'

// Environment specific SKU setup
var environmentConfigMap = {
  dev: {
    appServiceApp: {
      alwaysOn: false
    }
    appServicePlan: {
      sku: {
        name: 'F1'
        capacity: 1
      }
    }
  }
  prod: {
    appServiceApp: {
      alwaysOn: false // change to true before going live
    }
    appServicePlan: {
      sku: {
        name: 'F1'
        capacity: 1
      }
    }
  }
}

resource appServicePlan 'Microsoft.Web/serverfarms@2021-03-01' = {
  name: appServicePlanName
  location: resourceLocation
  sku: environmentConfigMap[environment].appServicePlan.sku
  tags: {
    env: environment
    asset: 'website'
  }
}
