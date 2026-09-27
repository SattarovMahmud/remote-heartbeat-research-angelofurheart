#include <stdio.h>
#include "esp_err.h"
#include "esp_wifi_types.h"
#include "esp_wifi.h"
#include "esp_event.h"
#include "esp_netif.h"
#include "nvs_flash.h"
#include "esp_log.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"

static void wifi_init(void)
{
    ESP_ERROR_CHECK(nvs_flash_init());
    ESP_ERROR_CHECK(esp_netif_init());
    ESP_ERROR_CHECK(esp_event_loop_create_default());

    wifi_init_config_t cfg = WIFI_INIT_CONFIG_DEFAULT();
    ESP_ERROR_CHECK(esp_wifi_init(&cfg));

    ESP_ERROR_CHECK(esp_wifi_set_mode(WIFI_MODE_STA));
    ESP_ERROR_CHECK(esp_wifi_start());

    ESP_LOGI("WIFI", "WiFi started");
}
static void wifi_csi_rx_cb(void *ctx, wifi_csi_info_t *info)
{
    printf("CSI packet received!\n");
}

void app_main(void)
{
    printf("\n");
    printf("=====================================\n");
    printf(" AngelOfUrHeart CSI Receiver Started\n");
    printf("=====================================\n");
    wifi_init();
    wifi_csi_config_t config = {
    .lltf_en = true,
    .htltf_en = true,
    .stbc_htltf2_en = true,
    .ltf_merge_en = true,
    .channel_filter_en = false,
    .manu_scale = false,
    .shift = false,
};

esp_err_t err;

err = esp_wifi_set_csi_config(&config);
printf("set_csi_config = %s (%d)\n", esp_err_to_name(err), err);

err = esp_wifi_set_csi_rx_cb(wifi_csi_rx_cb, NULL);
printf("set_csi_rx_cb = %s (%d)\n", esp_err_to_name(err), err);

err = esp_wifi_set_csi(true);
printf("set_csi = %s (%d)\n", esp_err_to_name(err), err);

printf("CSI Enabled!\n");

    while (1)
    {
        printf("Receiver is alive...\n");
        vTaskDelay(pdMS_TO_TICKS(1000));
    }
}