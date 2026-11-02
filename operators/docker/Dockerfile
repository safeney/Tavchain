FROM debian:bookworm-slim@sha256:a3bba7dc7dbcc1f37c2856c51fc9a7fac96608f50cb87b1b4e4d8b8c85ae988e
LABEL org.opencontainers.image.title="Tavchain full node"
LABEL org.opencontainers.image.version="1.8.1-tavchain.eval1-771002-docker1"
COPY bin/tavchaind /usr/local/bin/tavchaind
COPY network/ /opt/tavchain/network/
COPY notices/ /usr/share/doc/tavchain/
COPY init-node.sh /usr/local/bin/init-node
RUN printf '%s\n' 'fa434051778f277ba03454dde427aa2ec431a93a010b7ded3746edde50bb4991  /usr/local/bin/tavchaind' | sha256sum --check \
    && cd /opt/tavchain/network && sha256sum --check SHA256SUMS \
    && mkdir /data && chown 10001:10001 /data && chmod 0700 /data \
    && chmod 0755 /usr/local/bin/tavchaind /usr/local/bin/init-node
ENV HOME=/data
USER 10001:10001
WORKDIR /data
STOPSIGNAL SIGTERM
ENTRYPOINT ["/usr/local/bin/tavchaind"]
CMD ["version", "--long"]
